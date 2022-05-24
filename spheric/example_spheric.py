#!/usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

x= [0,1,1,0]
y= [0,0,1,0]

CO = 1.0
CA = 1.0

r = math.sqrt(2)
theta = math.tan(CO/CA)

print("[1,1] es equivalente a r="+str(r)+" theta = "+str(theta))

ax.plot(x,y)
circle1 = plt.Circle((0, 0), r, color='r',fill=False)
ax.add_patch(circle1)
ax.scatter([1],[1])
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.grid()


# r^2 = x^2 + y^2
# x= [-1.41, 1.41]
# y = sqrt(r^2 - x^2)


##X = np.arange(-r, r, 0.1)
##Y=[]
##for x in X:
##    if (r*r - x*x) >= 0.0:
##        Y.append(math.sqrt(r*r - x*x))
###print(len(X),len(Y))        
##ax.scatter(X,Y,color='b')
##X = np.arange(-r, r, 0.1)
##Y=[]
##for x in X:
##    if (r*r - x*x) >= 0.0:
##        Y.append(-math.sqrt(r*r - x*x))
##ax.scatter(X,Y,color='b')



dtheta = 2.0*math.pi / 12.0

THETA = np.arange(0.0, 2.0*math.pi, dtheta)

#x = r*sin(theta)
#y = r*cos(theta)
X=[]
Y=[]
for theta in THETA:
    X.append(r*math.sin(theta))
    Y.append(r*math.cos(theta))
    print(r,theta)
ax.scatter(X,Y,color='b')

def rho()

def r_vec(u,v):
    if v < 0:
        return rho(u,v)*math.cos(u/r0), v, rho(u,v)*math.sin(u/r0)
    else:
        sdfdsfdsfdsfsdf

U = np.arange(-1.0, 1.0, 0.1)
V = np.arange(-1.0, 1.0, 0.1)

for u,v in zip(U,V):
    print(u,v)

R = []
    
for u in U:
    for v in V:
        R.append(r_vec(u,v))
        print(u,v)

plot3D(R)
        
#THETA = np.arange(0.0, 2.0*math.pi, dtheta)
#PHI = np.arange(0.0, math.pi, dtheta)




#Omega






#plt.show()
