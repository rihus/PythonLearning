# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 07:40:37 2021

@author: riazh
"""

# Import functions that are needed
from tkinter import Text, Button, Frame, Label, Tk, filedialog   
from time import sleep
import random
#, VERTICAL, E, NS, Scrollbar, ttk,
import os
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.optimize import curve_fit

# Creating the splash screen object 
w_root = Tk()
w_root.title("WoW!")
w_width = 400
w_height = 150
monitor_width = w_root.winfo_screenwidth()
monitor_height = w_root.winfo_screenheight()
posw_x = (monitor_width / 2) - (w_width / 2)
posw_y = (monitor_height / 2) - (w_height / 2)
w_root.geometry(f'{w_width}x{w_height}+{int(posw_x)}+{int(posw_y)}')
## To hide the title bar
w_root.overrideredirect(True)
# Setting the Label
w_label = Label(w_root,text="WoW! \n Words of Wisdom",font="Arial 18 bold")
#wow_label = LabelFrame(w_root,text="WoW - Words of Wisdom", font = "Arial 22 bold italic")
w_label.pack(pady=30)
##Make and import a repository of quotes

def main_window():  
    # destory the splash screen window
    w_root.destroy()
    # Create new window again as above
    f_root = Tk()
    f_root.title("WoW!")
    f_width = 400
    f_height = 200
    monitor2_width = f_root.winfo_screenwidth()
    monitor2_height = f_root.winfo_screenheight()
    posf_x = (monitor2_width / 2) - (f_width / 2)
    posf_y = (monitor2_height / 2) - (f_height / 2)
    f_root.geometry(f'{f_width}x{f_height}+{int(posf_x)}+{int(posf_y)}')
    wow_feeling = Label(f_root,text="How are you feeling today?",font=24)
    wow_feeling.pack(pady=30)
    box_f = Frame(f_root)
    box_f.pack(side='top', pady=10)
    f_button1 = Button(box_f, text = 'Down', fg="red")
    f_button1.pack(side='left')
#    f_button1.pack(anchor='center', padx=20, pady=20)
    f_button2 = Button(box_f, text = 'Normal', fg="blue")
    f_button2.pack(side='left', padx=20)
    f_button3 = Button(box_f, text = 'Motivated', fg="green")
    f_button3.pack(side='left')
    
   
# Set Interval
w_root.after(3000,main_window)
# Execute tkinter 
w_root.mainloop()
