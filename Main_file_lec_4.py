# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:19:15 2025

@author: Malth
"""
## Main file ##

#equation 1 er density funktionen

import steady_state as steady
import numpy as np



def production_function(x,y): return x*y



#parameters:
    
delta = 1 #job destruction rate
rho = 100 #mathcing rate
r = 1 #ímpatience
n = 500 #number of types
tol = 1e-12 #tolerance level


steady.solve_model(n, delta, rho, r, production_function, tol)



