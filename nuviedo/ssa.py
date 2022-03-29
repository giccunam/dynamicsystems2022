
#TODO: Headers
#GNU 3.0 @ alexis.nuviedo@gmail.com


import numpy as np
import matplotlib.pyplot as plt


N_max=100

Xrange=np.arange(-N_max,N_max)
dx=1/N_max
dy=1/N_max
Xrange=Xrange*dx

Dx=[]
Dy=[]

for x in Xrange:
	l=np.sqrt(1-x*x)
	for y in np.arange(-l,l,dy):
		Dx.append(x)
		Dy.append(y)
		

T=np.arange(0,len(Dx))/len(Dx)

Xv=np.array(Dx)
Yv=np.array(Dy)

def F(t,x,y):
	return ((t*2)%1, 1/4*(x+2*np.cos(2*np.pi*t)), 1/4*(y+2*np.sin(2*np.pi*t)))

print(F(.5,.5,.5))
#plt.scatter(Xv,Yv)
#plt.show()

Tn,Xn,Yn=T,Xv,Yv

fig = plt.figure()
ax = fig.add_subplot()#(projection='3d')

for i in range(50):
	Tn,Xn,Yn=F(Tn,Xn,Yn)
	if(i%4==0):
		ax.scatter(Xn,Yn)#s,Tn)
plt.show()




