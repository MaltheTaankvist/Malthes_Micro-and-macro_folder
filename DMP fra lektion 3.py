# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:33:48 2025

@author: Malth
"""


#Package import:
from scipy.optimize import fsolve, least_squares
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

#et sted at samle mine plots
path = r"C:\Users\Malth\OneDrive\Dokumenter\GitHub\Malthes_Micro-and-macro_folder"

#definerer funktioner


def DMP_steady_state(X,*parameters):
    
    #unpack paramters
    b, p, r, c, delta, beta, alpha0, alpha1 = parameters
    
    
    w = X[0]
    u = X[1]
    v = X[2]
    
    theta = v/u
    lambda_var = alpha0 * theta**alpha1 #mathces per worker
    q = alpha0 * theta**-alpha1 #mathes per vacancy
    
    
    
    #print("wage",w)
    #print("unemployment rate:",u)
    #print("vacancy rate:",v)
    #vi behøver ikke at define out inden i Python
    
    out = np.zeros_like(X)
    
    out[0]=u-delta/(lambda_var+delta) #equilibrium unemployment
    out[1]=(p-w)/(r+delta)-c/q #job creation
    out[2]=w-b-beta*(p-b)-beta*c*theta #wage curve
    
    
    return out

#wage curve til tegning
def wage_curve(theta,parameters):
    w=b+beta*(p-b)+beta*c*theta
    return w

def job_creation(theta,parameters):
    q=alpha0*theta**(-alpha1)
    w=p-(c/q)*(r+delta)
    return w

#define parameters
b=0.4 #unemployment benefit
p=1 #productivity
r=0.0025 #discount rate
c=0.21 #vacancy rates
delta=0.01 #Employment rates
beta=0.5 #
alpha0=0.55
alpha1=0.5

parameters = (b,p,r,c,delta,beta,alpha0,alpha1)

#initial guess
initial_guess = [0.1,0.5,0.5]
initial_guess_array = np.array(initial_guess)

#set bounds
bounds=((0,0,0),(1,1,1)) #set bounds for each variable

#solve the model and print it with fsolve:
solution = fsolve(DMP_steady_state, initial_guess_array, args=parameters);
print(solution)

#solve med least squares hvor vi bruger bounds
solution2 = least_squares(DMP_steady_state, initial_guess_array, args=parameters,bounds=bounds)
print(solution2)

#Grafik
theta_grid = np.linspace(0.5,5,50)

fig1, ax1 =plt.subplots()
ax1.plot(theta_grid,wage_curve(theta_grid,parameters),label='wage curve')
ax1.plot(theta_grid,job_creation(theta_grid,parameters),label='job creation curve')
fig1.savefig(Path(path) / "DMP_plot.png", dpi=300)
plt.show()

