
#Smale's Solenoid Attractor - An attempt at a dynamic system attractor 
#visualization in py3
#Theorical model from Ergodic Dynamics (2021) by Jane Hawkings
#
#Copyright (C) 2022 Alexis H. Nuviedo Arriaga alexis.nuviedo@gmail.com
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
	ax.scatter(Xn,Yn,Tn,s=2)
	ax.set_xlim([-1,1])
	ax.set_ylim([-1,1])
	ax.set_zlim([-1,1])
	ax.view_init(elev=90, azim=np.pi)
	plt.savefig("images_attr/"+f"{i:03d}"+"-attrc.png")
	plt.clf()

print(len(Tn))
plots(Tn,Xn,Yn,0)
for i in range(50):
	nT=[]
	nX=[]
	nY=[]
	for t,x,y in zip(Tn,Xn,Yn):
		T,X,Y=F(t,x,y)
		nT.append(T)
		nX.append(X)
		nY.append(Y)
	Tn,Xn,Yn=nT,nX,nY
	plots(Tn,Xn,Yn,i+1)





