import random
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg as la
import math,cmath
from scipy.sparse import diags
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[0:10]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'red')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[10:20]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'blue')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[20:30]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'green')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[30:40]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'yellow')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[40:50]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'orange')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[50:60]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'purple')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[60:70]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'tab:cyan')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plot = np.loadtxt("current_file500.05.txt", dtype = 'float')[70:80]
gamma_str = np.loadtxt("x_axis.txt",dtype = 'float')
plt.scatter(gamma_str, plot, color = 'tab:purple')
plt.title('Tight-Binding Model')
plt.xlabel('$\mu_R - \mu_L$')
plt.ylabel('$\mathbf{I}$')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()