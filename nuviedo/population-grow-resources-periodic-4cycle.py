#!/usr/bin/env python3
#Author: alexis.nuviedo@gmail.com
#License: GNU GPL 3.0.
#No warranty or liability assumed irrelevant of thermonuclear wars or lack thereof.


import matplotlib.pyplot as plt
import numpy as np
fig, ax=plt.subplots()


x0=40/51 #a=x*(r/rho)
#x=(1+rc)/r * a
c=10
r=.255
rho=1+r*c
a0=x0*r/rho#x0*(r/rho)

a=a0
X=[]
X.append(rho/r*a)
for i in np.arange(0,26):
   a=rho*a*(1-a)
   X.append((rho)/(r)*a)
ax.plot(X,linewidth=2.0)#, label=("({:.02f},{:.02f})").format(a0,c))



#plt.legend()
plt.title("Periodic rho*a(1-a)")
plt.savefig("population-grow-resources-periodic-4cycle.png")
plt.show()
