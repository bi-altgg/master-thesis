import random
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg as la
import math,cmath
from scipy.sparse import diags
from scipy.optimize import curve_fit
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
s= 15
colormark =[['green',"o"],['blue',"."],['red',"^"],['tab:grey',"v"]]
def func(x, a, b):

    return x**(-a) + b
ax1 = plt.subplot(141)
sgstrn = [0.00,-1.50]
fitsite = [2.0,2.0]
for i in range(2):
    plot = np.loadtxt('(0.0)conductivity v_s strength_at_energy'+'%1.2f'%sgstrn[i]+'.txt', dtype = 'float')
    keep_point = np.where(plot > 1.0E-18)
    plot=plot[keep_point]
    gamma_str = np.loadtxt('x-axis.txt',dtype = 'float')
    gamma_str=gamma_str[keep_point]
    fittingx = np.loadtxt('x-axis.txt',dtype = 'float')
    keep_point2 = np.where(fittingx > fitsite[i])
    fittingx = fittingx[keep_point2]
    fittingy = np.loadtxt('(0.0)conductivity v_s strength_at_energy'+'%1.2f'%sgstrn[i]+'.txt', dtype = 'float')
    fittingy = fittingy[keep_point2]
    popt, pcov = curve_fit(func, fittingx, fittingy, maxfev=300000)
    plt.plot(fittingx, func(fittingx, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
    plt.scatter(gamma_str, plot,s,c = colormark[i][0],marker = colormark[i][1],alpha = .8,label =  f'$\epsilon_F = {sgstrn[i]}$')
    plt.title('($\lambda = 0.5$)')
    plt.xlabel('$\gamma$')
    plt.ylabel('$G/G_o$')
    plt.grid(True)
    plt.legend()
ax1 = plt.subplot(142)
sgstrn = [0.00]
fitsite = [3.0,0.0]
for i in range(1):
    plot = np.loadtxt('(0.5)conductivity v_s strength_at_energy'+'%1.2f'%sgstrn[i]+'.txt', dtype = 'float')
    print(plot)
    keep_point = np.where(plot > 1.0E-18)
    plot=plot[keep_point]
    gamma_str = np.loadtxt('x-axis.txt',dtype = 'float')
    gamma_str=gamma_str[keep_point]
    fittingx = np.loadtxt('x-axis.txt',dtype = 'float')
    keep_point2 = np.where(fittingx > fitsite[i])
    fittingx = fittingx[keep_point2]
    fittingy = np.loadtxt('(0.5)conductivity v_s strength_at_energy'+'%1.2f'%sgstrn[i]+'.txt', dtype = 'float')
    fittingy = fittingy[keep_point2]
    popt, pcov = curve_fit(func, fittingx, fittingy, maxfev=300000)
    plt.plot(fittingx, func(fittingx, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
    plt.scatter(gamma_str, plot,s,c = colormark[i][0],marker = colormark[i][1],alpha = .8,label =  f'$\epsilon_F = {sgstrn[i]}$')
    plt.title('($\lambda = 0.5$)')
    plt.xlabel('$\gamma$')
    plt.ylabel('$G/G_o$')
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.legend()
sgstrn = [0.00,-1.87]
fitsite = [10.0,10.0]
ax2 = plt.subplot(143)
for i in range(2):
    plot = np.loadtxt('(1.0)conductivity v_s strength_at_energy'+'%1.2f'%sgstrn[i]+'.txt', dtype = 'float')
    keep_point = np.where(plot > 1.0E-18)
    plot=plot[keep_point]
    gamma_str = np.loadtxt('x-axis.txt',dtype = 'float')
    gamma_str=gamma_str[keep_point]
    fittingx = np.loadtxt('x-axis.txt',dtype = 'float')
    keep_point2 = np.where(fittingx > fitsite[i])
    fittingx = fittingx[keep_point2]
    fittingy = np.loadtxt('(1.0)conductivity v_s strength_at_energy'+'%1.2f'%sgstrn[i]+'.txt', dtype = 'float')
    fittingy = fittingy[keep_point2]
    popt, pcov = curve_fit(func, fittingx, fittingy, maxfev=300000)
    plt.plot(fittingx, func(fittingx, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
    plt.scatter(gamma_str, plot,s,c = colormark[i][0],marker = colormark[i][1],alpha = .8,label =  f'$\epsilon_F = {sgstrn[i]}$')
    plt.title('($\lambda = 1.0$)')
    plt.xlabel('$\gamma$')
    plt.ylabel('$G/G_o$')
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.legend()
sgstrn = [0.000,-0.011,-0.137,-0.143]
ax3 = plt.subplot(144)
for i in range(4):
    plot = np.loadtxt('(1.2)conductivity v_s strength_at_energy'+'%1.3f'%sgstrn[i]+'.txt', dtype = 'float')
    keep_point = np.where(plot > 1.0E-18)
    plot=plot[keep_point]
    gamma_str = np.loadtxt('x-axis.txt',dtype = 'float')
    gamma_str=gamma_str[keep_point]
    plt.scatter(gamma_str, plot,s,c = colormark[i][0],marker = colormark[i][1],alpha = .8,label =  f'$\epsilon_F = {sgstrn[i]}$')
    plt.title('($\lambda = 1.2$)')
    plt.xlabel('$\gamma$')
    plt.ylabel('$G/G_o$')
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.legend()
plt.show()
