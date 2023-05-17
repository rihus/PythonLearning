# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:07:06 2023

@author: HUSDQ4
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(1, 35))
fig.subplots_adjust(bottom=0.1)

cmap = mpl.cm.jet
norm = mpl.colors.Normalize(vmin=0.0, vmax=1)

cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
             cax=ax, orientation='vertical')
cbar.ax.tick_params(size = 22, width=6) # cb.outline.set_linewidth(2)
cbar.set_ticks([0,0.5,1])
cbar.set_ticklabels([0.0,0.5,1.0])
cbar.outline.set_linewidth(6)
plt.setp(cbar.ax.yaxis.get_ticklabels(), fontsize=120) # weight='bold',

#%%