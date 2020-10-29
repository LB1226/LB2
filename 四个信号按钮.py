import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import tkinter as tk
from tkinter import ttk

def tk1(): 
    def x(t):
        return np.exp(-t) * np.cos(8 * t - 200)

    fig = plt.figure(figsize=(10, 8), dpi=80)
    ax1 = axisartist.Subplot(fig, 111)
    fig.add_axes(ax1)

    ax1.axis[:].set_visible(False)
    ax1.axis["x"] = ax1.new_floating_axis(0, 0)

    ax1.axis["x"].set_axisline_style("->", size=1.0)
    ax1.axis["y"] = ax1.new_floating_axis(1, 0)
    ax1.axis["y"].set_axisline_style("->", size=1.0)
    ax1.axis["x"].set_axis_direction("top")
    ax1.axis["y"].set_axis_direction("right")

    plt.xlim(-4, 4)
    plt.ylim(-100, 100)

    t = np.arange(-4, 4, 0.01)
    plt.plot(t, x(t), 'r-')
    plt.title('x(t)=cos(ωt+θ)*e**(σt)')
    plt.xlabel('t')
    plt.show()

 
 
def tk2():
     def x(t):
         return np.exp(-t)*np.cos(8*t-200)

     fig = plt.figure(figsize=(10, 8),dpi=80)
     ax1= axisartist.Subplot(fig, 111)
     fig.add_axes(ax1)

     ax1.axis[:].set_visible(False)
     ax1.axis["x"] = ax1.new_floating_axis(0,0)

     ax1.axis["x"].set_axisline_style("->", size = 1.0)
     ax1.axis["y"] = ax1.new_floating_axis(1,0)
     ax1.axis["y"].set_axisline_style("->", size = 1.0)
     ax1.axis["x"].set_axis_direction("top")
     ax1.axis["y"].set_axis_direction("right")

     plt.xlim(-4,4)
     plt.ylim(-100,100)

     t=np.arange(-4,4,0.01)
     plt.plot(t,x(t),'r-')
     plt.title('x(t)=cos(ωt+θ)*e**(σt)')
     plt.xlabel('t')
     plt.show()     

def tk3():
    a=1

    plt.figure(figsize=(8,5), dpi=80)
    ax = plt.subplot(111)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    x = np.arange(-2, 2, 0.1)
    y1 = pow(2,a*x)
    y2 = pow(2,-a*x)
    y3 = pow(2,0*x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.show()

def tk4():
    plt.figure(figsize=(8,5), dpi=80)

    plt.xlabel("t")
    plt.ylabel("x(t)")
    ax = plt.subplot(111)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    x = np.arange(-2*np.pi, 2*np.pi, 0.1 )
    y1=np.cos(x)
    y2=np.sin(x)

    plt.plot(x, y1)
    plt.plot(x, y2)

    plt.show()

def button():
    win = tk.Tk()

    win.geometry("600x500")
    win.title('GUI004')

    aLabel = ttk.Label(win, text='按钮')
    aLabel.grid(column=0, row=0)

    action1 = ttk.Button(win, text='幅度增长的正弦信号',command=tk1)
    action1.grid(column=1, row=0)
    action2 = ttk.Button(win, text='幅度衰减的正弦信号',command=tk2)
    action2.grid(column=2, row=0)
    action3 = ttk.Button(win, text='实指数信号',command=tk3)
    action3.grid(column=3, row=0)
    action4 = ttk.Button(win, text='正弦信号',command=tk4)
    action4.grid(column=4, row=0)

button()