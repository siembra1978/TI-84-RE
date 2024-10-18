# Written by siembra1978
import matplotlib.pyplot as plt
import numpy as np
import config
from frange import frangef

# Sets window settings
xmin = config.minX # Sets Minimum X Value
xmax = config.maxX # Sets Maximum X Value
ymin = config.minY # Sets Minimum Y Value
ymax = config.maxY # Sets Maximum Y Value
step = config.step # Sets the step of the X values used

# Sets actual X axis maximum to fix PLT's weird handling of the windows
amax = xmax + 1

# Function That Uses Data From solve() to Graph with PLT
def graph(xsolu, ysolu):
    x = np.linspace(0.2, 10, 100)
    fig, ax = plt.subplots()
    ax.grid(True, which='both')

    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    plt.plot(xsolu, ysolu)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid(visible=True)
    plt.show()

# Calculates Y Values using the function given by enter() by replacing 'x' with all the numbers with the ranges set in window settings
def solve(funcs, x):
    a = funcs.replace("x", str(x))
    b = eval(a)
    #print(b)
    return b

# Controls the order of sequences when a function is given
def enter(func):

    xsolu = []
    ysolu = []

    for x in frangef(xmin, xmax, step):
        ysol = solve(func, x)
        xsolu.append(x)
        ysolu.append(ysol)

    graph(xsolu,ysolu)

