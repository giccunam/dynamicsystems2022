#!/usr/bin/env python3
#Author: alexis.nuviedo@gmail.com
#License: GNU GPL 3.0.
#No warranty or liability assumed irrelevant of thermonuclear wars or lack thereof.

import matplotlib.pyplot as plt

N=100

fig, ax=plt.subplots()

for x0 in range(1):
    for a in range(1):
        for b in range(5):
            X=[]
            x=x0+1
            X.append(x)
            for i in range(N):
                x=(1/(b+1))*x+a+1
                X.append(x)
            ax.plot(X,linewidth=2.0)

#plt.legend()
plt.show()
