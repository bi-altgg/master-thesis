#AAH critical
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg as la
import math,cmath
from scipy.sparse import diags
#Creating the spectral density matrix
n=11;#laatice sites
no=6;#bath lattice point
b = (1+np.sqrt(5))/2
sitegammaindx = [0, n-1,no-1]
lowval = np.logspace(-2,0,100)
highval = np.logspace(0,3,1000)
gammastrn = [*lowval,*highval]
arrayofsitegamstrn = []
for i in gammastrn:
    sitegammastrn = [1.0,1.0,i]
    arrayofsitegamstrn += [sitegammastrn]
to = 3.0 #bath tunneling potential
t = 1.0 #system hopping
lamba = 0.0
alpha = 0.0
#sitepotential = 0.0;#bath site potential(constant)
siteindx = np.array(range(1, n+1))
sitepotentialAAH = 2*lamba*np.cos(2*np.pi*b*(siteindx))/(1+alpha*np.cos(2*np.pi*b*(siteindx)))
def selfenergy(gamma,energy):
    mat = ((gamma**2)/(2*to**2))*(energy - np.sqrt(4*to**2-energy**2)*1j)
    return mat
def specden(gamma,site,energy):#spectral density matrix(-2Im(sigma))
    mat = np.zeros((n,n),dtype = 'complex_')
    mat[site,site] =  -2*(selfenergy(gamma,energy).imag)
    return mat
#Green's functions
def ret_gre(energy, arraysitgamstrn):
    k = [np.ones(n-1),np.ones(n),np.ones(n-1)]
    offset = [-1,0,1]
    mat = diags(k,offset,dtype='complex_').toarray()
    for i in range(n):
        mat[i, i] = (energy - sitepotentialAAH[i]) / t
    for i in range(3):
        mat[sitegammaindx[i],sitegammaindx[i]] = (energy - sitepotentialAAH[sitegammaindx[i]] - selfenergy(arraysitgamstrn[i],energy))/t
    return (np.linalg.inv(mat)/t)


def adv_gre(energy, arraysitegamstrn):
    return np.transpose(np.conjugate(ret_gre(energy, arraysitegamstrn)))
E_f = np.loadtxt('eigenvalue(0.0)11.dat')
#transmission probability
def trnasmission(sgindx1,sgstrn1,sgindx2,sgstrn2,energy, arraysitegamstrn):
    spcdn1 = specden(sgstrn1,sgindx1,energy)
    retgre = ret_gre(energy, arraysitegamstrn)
    spcdn2 = specden(sgstrn2,sgindx2,energy)
    advgre = adv_gre(energy, arraysitegamstrn)
    mat = np.dot(np.dot(spcdn1,retgre),np.dot(spcdn2,advgre))
    return np.trace(mat)
mat = []
for sgstrn in arrayofsitegamstrn:
    fe = E_f[0]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[1]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[2]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat = []
for sgstrn in arrayofsitegamstrn:
    fe = E_f[3]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[4]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[5]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat = []
for sgstrn in arrayofsitegamstrn:
    fe = E_f[6]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[7]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[8]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat = []
for sgstrn in arrayofsitegamstrn:
    fe = E_f[9]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.2f'%fe+'.txt',plot)
mat=[]
for sgstrn in arrayofsitegamstrn:
    fe = E_f[10]
    print(sgstrn,fe)
    rl = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    nr = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[1],sgstrn[1],fe, sgstrn).real
    nl = trnasmission(sitegammaindx[2],sgstrn[2],sitegammaindx[0],sgstrn[0],fe, sgstrn).real
    rn = trnasmission(sitegammaindx[1],sgstrn[1],sitegammaindx[2],sgstrn[2],fe, sgstrn).real
    if nr + nl == 0:
        mat += [rl]
    else:
        mat += [(rl+((rn*nl)/(nr+nl)))]
plot = [m if m>1.0E-18 else 1.0E-18 for m in mat]
np.savetxt('(0.0)conductivity v_s strength_at_11_site'+'%1.3f'%fe+'.txt',plot)
np.savetxt('(0.0)x-axis11.txt', gammastrn)
