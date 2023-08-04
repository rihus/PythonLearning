# -*- coding: utf-8 -*-
"""
Created on Sat Aug 1 10:37:06 2023

@author: Riaz Hussain, PhD
"""
#%%
import matplotlib.pyplot as plt
import numpy as np

mHe3 = 3.016029 * 1.66053904e-27 # kg
mO2 = 31.998* 1.66053904e-27 # kg
mu = (mHe3 * mO2)/(mHe3 + mO2) # kg
S = 1
gamma_He3 = -20.3801587e7 # (rad T‑1 s-1)
gamma_O = -3.62808e7 # (rad T‑1 s-1)
h_bar = 1.054571817e-34 # J⋅s
d = 3.1e-10 # meters
kb = 1.380649e-23 # J/K
T = 299 # K

invT1 = (16/3)*S*(S+1)*(gamma_He3**2)*(gamma_O**2)*(h_bar**2/d**2)*(np.sqrt((np.pi*mu)/(8*kb*T)))*2.6867811e25

print("1/T1 is: ", invT1)

#%%