# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:03:23 2021

@author: riazh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##NMR spectrum measurement data I'm using here was taken during my PhD on
##a molecular nanomagnet Yb(trensal) - published as Riaz Hussain et al., JACS, 2018
gau_data = np.genfromtxt("Yb_trensal.ascii", dtype=None)

#Makeing the arrays of data
x = np.asarray(gau_data[:,0])
y = np.asarray(gau_data[:,1])
##Plotting the data
plt.plot(x,y, 'ob', label='Yb_data')
##Defining a  double gaussian function 
def bi_gau(x,Amp1,centr1,mu1,Amp2,centr2,mu2):
    func = Amp1*np.exp(-(x-centr1)**2/(2*mu1**2)) \
           + Amp2*np.exp(-(x-centr2)**2/(2*mu2**2))
    return func
##Fitting using curve_fit. initial guess are by looking at the plot
popt,pcov = curve_fit(bi_gau,x,y, p0=[90000, 389, 1, 120000, 488, 1])
##Plotting the fit
plt.plot(x,bi_gau(x,*popt),'--r',label='gau_fit')
plt.legend(loc='best')
plt.title('Gaussian fit on experimental NMR data for Yb(trensal)')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Intensity (arb. units)')
plt.show()