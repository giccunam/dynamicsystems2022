#!/usr/bin/env python3
#Author: alexis.nuviedo@gmail.com
#License: GNU GPL 3.0.
#No warranty or liability assumed irrelevant of thermonuclear wars or lack thereof.


import matplotlib.pyplot as plt
import numpy as np
fig, ax=plt.subplots()


x0=15
r=.01
for x0 in np.arange(5,41,5):
    for c in np.arange(1,21,2):
        #c=10
        rho=1+r*c

        a=r/rho*x0

        X=[]
        X.append(rho/r*a)


        iterations=np.arange(0,30)
        for i in iterations:
            a=rho*a*(1-a)
            X.append(rho/r*a)
        ax.plot(X,linewidth=2.0, label=("({:.02f},{:.02f})").format(x0,c))

#plt.legend()
plt.title("x=px(1-x), p=1+rc")
plt.savefig("population-grow-resources.png")
plt.show()
