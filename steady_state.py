# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:29:40 2025

@author: Malth
"""
import steady_state as steady
import numpy as np

def solve_model(n, delta, rho, r, production_function, tol):
    theta = rho/(2*(r+delta))
    #x = np.linspace(0.000001, 0.999999, n)
    #y = np.linspace(0.000001, 0.999999, n)
    grid = np.linspace(1/n/2, 1-1/n/2, n)
    
    payoffs = np.empty([n,n])
    for i in range(n):
        x=grid[i]
        for j in range(n):
            y=grid[j]
            payoffs[i,j] = production_function(x,y)
    return payoffs
        
            
    
    #x er tal mellem 0 og 1
    #lav matrix der er 500*500
    