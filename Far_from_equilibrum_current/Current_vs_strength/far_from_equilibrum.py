import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import math,cmath
from scipy.sparse import diags
from scipy.integrate import quad
from mpmath import *
from scipy import integrate
from scipy import optimize
from scipy.misc import derivative

Nmst = 200; #Number of lattice points
Pbst = 100;#Probe attachment site
lbd = 0.0 ;#Lambda strength ofAAH
irrb = (1 + np.sqrt(5))/2
t = 1.0; # hopping potential for sites
to = 3.0; # hopping potential for bath
sitegammaindx = [0, Nmst-1, Pbst-1]
gammastrn = np.logspace(-2,2,100)
arrayofsitegamstrn = []
for i in gammastrn:
    sitegammastrn = [1.0,1.0,i]
    arrayofsitegamstrn += [sitegammastrn]
siteindx = np.array(range(1, Nmst+1))
sitepotential = 2*lbd*np.cos(2*np.pi*irrb*(siteindx))
diagonals = [sitepotential,t*np.ones(Nmst-1), t*np.ones(Nmst-1)]
offset = [0,-1,1]
sys_Ham = diags(diagonals,offset,dtype='complex_').toarray()
mu_L = 0.1
mu_R = [0.15,0.55,1.05,1.55,10.05,50.05,100.05,500.05]
beta_left = 1/100
beta_right = 1/100
beta_probe = 1/100
def bosonic_distribution(mu, energy, beta):#bosonic distribution function
    return (np.exp(beta*(energy - mu))+1)**(-1)
def selfenergy(gamma,site,energy):#self energy matrix
    mat = np.zeros((Nmst,Nmst),dtype = 'complex_')
    mat[site,site] =  ((gamma**2/(2*to**2))*(energy - cmath.sqrt(4*to**2-energy**2)*1j))
    return mat
def specden(gamma,energy):#spectral density matrix(-2Im(sigma))
    mat =  -2*((gamma**2/(2*to**2))*(energy - cmath.sqrt(4*to**2-energy**2)*1j)).imag
    return mat
def Green_func(energy,  arraysitgamstrn):#green's function
    mat = energy*np.identity(Nmst) - sys_Ham - selfenergy( arraysitgamstrn[0],sitegammaindx[0],energy) - \
    selfenergy( arraysitgamstrn[1],sitegammaindx[1],energy) - selfenergy( arraysitgamstrn[2],sitegammaindx[2],energy)
    return (np.linalg.det(mat)/t)
def advan_gren(energy):
    mat = np.transpose(np.conjugate(Green_func(energy)))
    return mat
def transmissionprob(sitstrn1, sitstrn2, energy,  arraysitegamstrn):
    spcdn1 = specden(sitstrn1, energy)
    retgre = Green_func(energy,  arraysitegamstrn)
    spcdn2 = specden(sitstrn2, energy)
    mat = (spcdn1*spcdn2)/(abs(retgre)**2)
    return mat
vtransmissionprob = np.vectorize(transmissionprob)
vtransmissionprob.excluded.add(3)
point = np.linspace(-5.0,5.0, 1500)
for i in range(len(mu_R)):
    print(mu_R[i])
    mat = []
    for sgstrn in arrayofsitegamstrn:
        print(sgstrn)
        first_trans_probe  = vtransmissionprob(sgstrn[2], sgstrn[0],point, sgstrn)
        second_trans_probe = vtransmissionprob(sgstrn[2], sgstrn[1],point, sgstrn)
        first_trans_right  = vtransmissionprob(sgstrn[1], sgstrn[0],point, sgstrn)
        second_trans_right = vtransmissionprob(sgstrn[1], sgstrn[2],point, sgstrn)
        def current_val(mu_p,mu_l,mu_r):#integral equation
            left_bath = bosonic_distribution(mu_l, point, beta_left)
            probe = bosonic_distribution(mu_p, point, beta_probe)
            right_bath = bosonic_distribution(mu_r, point, beta_right)
            return first_trans_probe*(probe - left_bath) + second_trans_probe*(probe - right_bath)
        def current_int(mu_p,mu_l,mu_r):
            point = np.linspace(-5.0,5.0,1500)
            current_val2 = np.vectorize(current_val)
            I = current_val2(mu_p,mu_l,mu_r)
            return(integrate.simps(I,point))
        def deriv_current(mu_p,mu_l,mu_r) :
            return derivative(lambda x: current_int(x,mu_l,mu_r),mu_p)
        def min_probe_potential(mu_l,mu_r):#Newton-Raphson minimization
            Mu = (mu_r+mu_l)/2
            current =  current_int(Mu,mu_l,mu_r)
            while abs(current) >= 1.0e-10:
                Mu = Mu - (current_int(Mu,mu_l,mu_r)/(deriv_current(Mu,mu_l,mu_r)))
                current =  current_int(Mu,mu_l,mu_r)
            return Mu
        def current_full(mu_l, mu_r):
            mu_poi = min_probe_potential(mu_l,mu_r)
            left_bath = bosonic_distribution(mu_l, point, beta_left)
            probe = bosonic_distribution(mu_poi, point, beta_probe)
            right_bath = bosonic_distribution(mu_r, point, beta_right)
            return first_trans_right*(right_bath - left_bath) + second_trans_right*(right_bath - probe)
        point = np.linspace(-5.0,5.0,1500) 
        current_temp = np.vectorize(current_full)
        def current_full2(mu_l,mu_r):  
            point = np.linspace(-5.0,5.0,1500) 
            current_temp = np.vectorize(current_full)
            I = current_temp(mu_l, mu_r)
            return(integrate.simps(I,point))
        print(sgstrn)
        mat.append(current_full2(mu_L,mu_R[i]))
    np.savetxt("current_file" + str(mu_R[i]) + '.txt', mat )
np.savetxt("x_axis.txt", gammastrn)