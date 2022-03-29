#!/usr/bin/env python3
#Author: alexis.nuviedo@gmail.com
#License: GNU GPL 3.0.
#No warranty or liability assumed irrelevant of thermonuclear wars or lack thereof.


import matplotlib.pyplot as plt
fig, ax=plt.subplots()


print("x=(1+r)x")
X=[]
x0=2
x=x0
r=.1
X.append(x)
for i in range(1000):
    x=x*(1+r)
    X.append(x)

ax.plot(X,linewidth=2.0, label=("({:.02f},{:.02f})").format(x0,r))

plt.legend()
plt.title("x=(1+r)x")
plt.savefig("population-grow.png")
plt.yscale("log")
plt.show()
