#!/usr/bin/env python3
#Author: alexis.nuviedo@gmail.com
#License: GNU GPL 3.0.
#No warranty or liability assumed irrelevant of thermonuclear wars or lack thereof.


import matplotlib.pyplot as plt
import numpy as np
fig, ax=plt.subplots()


print("x=(1+r)x")
X0=np.arange(100,1000,200)

for x0 in X0:
    X=[]
    x=x0
    r=.1
    X.append(x)

    for i in range(100):
        x=x*(1+r)
        X.append(x)

    ax.plot(X,linewidth=2.0, label=("({:.02f},{:.02f})").format(x0,r))

plt.legend()
plt.title("x=(1+r)x")
plt.savefig("population-grow-different-initial-conditions.png")
#plt.yscale("log")
plt.show()
