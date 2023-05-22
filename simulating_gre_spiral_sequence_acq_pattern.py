# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:34:16 2023

@author: HUSDQ4
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#%%
r = 12.5  # outer radius
a = 0  # inner radius
b = 0.5  # increment per revolution
n = (r - a) / b  # number of revolutions
th = 2 * n * np.pi  # angle
Th = np.linspace(0, th, 1 * 720)  # angle values 1250

x = (a + b * Th / (2 * np.pi)) * np.cos(Th)  # x coordinates
y = (a + b * Th / (2 * np.pi)) * np.sin(Th)  # y coordinates

fig, ax = plt.subplots()

# Initialize the line object
line, = ax.plot([], [], 'b')

# Set the limits of the plot
ax.set_xlim(-r, r)
ax.set_ylim(-r, r)

# Function to update the line data
def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=len(x), interval=1)

# Save the animation as a GIF file
animation.save('spiral.gif', writer='pillow')

# Show the plot (optional)
plt.show()

#%%


r = 12.5  # outer radius
a = 0  # inner radius
b = 0.5  # initial increment per revolution
n = (r - a) / b  # number of revolutions
th = 2 * n * np.pi  # angle
Th = np.linspace(0, th, 1 * 720)  # angle values

x = (a + b * Th / (2 * np.pi)) * np.cos(Th)  # x coordinates
y = (a + b * Th / (2 * np.pi)) * np.sin(Th)  # y coordinates

fig, ax = plt.subplots()

# Initialize the line object
line, = ax.plot([], [], 'b')

# Set the limits of the plot
ax.set_xlim(-r, r)
ax.set_ylim(-r, r)
# Remove ticks and tick labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.xlabel('$k_x \\ \longrightarrow$', fontsize=24)
plt.ylabel('$k_y \\ \longrightarrow$', fontsize=24)
# Function to update the line data
def update(frame):
    global b
    line.set_data(x[:frame], y[:frame])

    # Gradually increase the distance between revolutions
    if frame % 10 == 0:
        b += 0.1

    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=len(x), interval=1)

# Save the animation as a GIF file
animation.save('spiral.gif', writer='pillow')

# Show the plot (optional)
plt.show()

#%%Simulating Cartesian sequence scheme

# Create the figure and axis
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Remove ticks and tick labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.xlabel('$k_x \\ \longrightarrow$', fontsize=24)
plt.ylabel('$k_y \\ \longrightarrow$', fontsize=24)

# Initialize the lines
lines = []

# Function to initialize the lines
def init():
    for i in range(num_lines):
        line, = ax.plot([], [])
        lines.append(line)
    return lines

# Function to update the lines
def update(frame):
    for i in range(frame + 1):
        line = lines[i]
        x = np.array([0, 10])
        y = np.array([10 - line_distance * i, 10 - line_distance * i])
        line.set_data(x, y)
    return lines

# Define the number of lines and their distance
num_lines = 25
line_distance = 0.4

# Create the animation
animation = FuncAnimation(fig, update, init_func=init, frames=num_lines, interval=35)

# Save the animation as a GIF file
animation.save('gre.gif', writer='pillow')

# Show the plot (optional)
plt.show()

#%%