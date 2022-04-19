
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

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')

def plots(Tn,Xn,Yn,i):
	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.scatter(Xn,Yn,Tn)
	ax.set_xlim([0,1])
	ax.set_ylim([-1,1])
	ax.set_zlim([-1,1])
	plt.savefig("images_attr/"+f"{i:03d}"+"-attrc.png")


plots(Tn,Xn,Yn,0)
for i in range(60):
	#_=[]
	Xf=[]
	Yf=[]
	for j in range(len(Tn)):
		_,x,y=F(Tn[j],Xn[j],Yn[j])
		Xf.append(x)
		Yf.append(y)
	Xn,Yn=Xf,Yf
	plots(Tn,Xn,Yn,i+1)




