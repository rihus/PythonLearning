# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:07:06 2023

@author: HUSDQ4
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(1, 10))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.jet
norm = mpl.colors.Normalize(vmin=4, vmax=44)

cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
             cax=ax, orientation='vertical')
#cbar.ax.tick_params(size = 5, labelsize=16)
plt.setp(cbar.ax.yaxis.get_ticklabels(), weight='bold', fontsize=18)

#%%