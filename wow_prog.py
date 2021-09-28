# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 07:40:37 2021

@author: riazh
"""

# Import functions that are needed
from tkinter import *
from tkinter import messagebox
# from time import sleep
import random
#, VERTICAL, E, NS, Scrollbar, ttk,
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.optimize import curve_fit

# Creating the splash screen object 
w_root = Tk()
w_root.title("WoW!")
w_width = 500
w_height = 250
monitor_width = w_root.winfo_screenwidth()
monitor_height = w_root.winfo_screenheight()
posw_x = (monitor_width / 2) - (w_width / 2)
posw_y = (monitor_height / 2) - (w_height / 2)
w_root.geometry(f'{w_width}x{w_height}+{int(posw_x)}+{int(posw_y)}')
## To hide the title bar
w_root.overrideredirect(True)
# Setting the Label
w_label = Label(w_root,text="WoW! \n Words of Wisdom",font="Arial 32 bold", pady=20)
#wow_label = LabelFrame(w_root,text="WoW - Words of Wisdom", font = "Arial 22 bold italic")
w_label.pack(pady=30)
##Make and import a repository of quotes

def down_button():
    f=open('down_feeling.txt')
    lines = f.readlines()
    randq_d=random.choice(lines)
    messagebox.showinfo("Remember!", randq_d)
def normal_button():
        f=open('normal_feeling.txt')
        lines = f.readlines()
        randq_n=random.choice(lines)
        messagebox.showinfo("Remember!", randq_n)
def motivated_button():
        f=open('motivated_feeling.txt')
        lines = f.readlines()
        randq_m=random.choice(lines)
        messagebox.showinfo("Remember!", randq_m)

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
    f_button1 = Button(box_f, text = 'Down', fg="red", command=down_button)
    f_button1.pack(side='left')
#    f_button1.pack(anchor='center', padx=20, pady=20)
    f_button2 = Button(box_f, text = 'Normal', fg="blue", command=normal_button)
    f_button2.pack(side='left', padx=20)
    f_button3 = Button(box_f, text = 'Motivated', fg="green", command=motivated_button)
    f_button3.pack(side='left')
    # button_quit=Button(box_f, text='Exit', command=f_root.quit)
    # button_quit.pack(side='bottom')
  
# Set Interval
w_root.after(3000,main_window)
# Execute tkinter 
w_root.mainloop()