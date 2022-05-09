import numpy as np
import matplotlib.pyplot as plt

def lerp(x,y,t):
	return x + (y-x)*t

def dist(P0,P1):
	dx=P1[0]-P0[0]
	dy=P1[1]-P0[1]
	return np.sqrt(dx**2+dy**2)

class line:
	P0=None
	P1=None
	m=None
	sz=None
	def __init__(self,p0,p1):
		self.P0=p0
		self.P1=p1
		self.sz=dist(p0,p1)
		if(p0[1]==p1[1]):
			self.m=0
			return
		self.m=(p1[1]-p0[1])/(p1[0]-p0[0])
		
	def midp(self):
		return (lerp(self.P0[0],self.P1[0],1/2),lerp(self.P0[1],self.P1[1],1/2))
	def split(self):
		p0=self.P0
		p1=(lerp(self.P0[0],self.P1[0],1/3),lerp(self.P0[1],self.P1[1],1/3))
		p2=(lerp(self.P0[0],self.P1[0],2/3),lerp(self.P0[1],self.P1[1],2/3))
		p3=self.P1
		return p0,p1,p2,p3
	
class ftriangle:
	L=None
	P0=None
	P1=None
	m=None
	l=None
	
	def __init__(self,L):
		self.L=L
		self.P0=L.P0
		self.P1=L.P1
		self.PM=L.midp()
		self.m=L.m
		self.l=L.sz
	
	def getp(self):
		theta=np.arctan(self.m)
		gamma=np.arctan2(self.P1[1]-self.P0[1],self.P1[0]-self.P0[0])+np.radians(90)
		h=np.sqrt(self.l**2-(self.l/2)**2)
		p1=self.P0
		p2=self.P1
		#print(np.cos(gamma),np.sin(gamma))
		p3=(self.PM[0]+h*np.cos(gamma),self.PM[1]+h*np.sin(gamma))
		return p1,p3,p2#,p1
		
	def toLines(self,skipL=False):
		p1,p3,p2=self.getp()
		L1=line(p1,p3)
		L2=line(p3,p2)
		if(skipL):
			return L1,L2
		L3=line(p2,p1)
		return L1,L2,L3

def Fractal(P0,ilen,l):
	Ls=[]
	Ts=[]
	T0=ftriangle(line(P0,(P0[0]+l,P0[1])))
	Ts.append(T0)
	for l in T0.toLines():
		Ls.append(l)
		
	for i in range(ilen):
		L2=[]
		for j in range(len(Ls)):
			l=Ls[j]
			p0,p1,p2,p3=l.split()
			La=line(p0,p1)
			Lb=line(p1,p2)
			Lc=line(p2,p3)
			
			L2.append(La)
			
			T=ftriangle(Lb)
				
			Ts.append(T)
			for l in T.toLines(True):
				L2.append(l)
			
			L2.append(Lc)
		Ls=L2
	Px=[]
	Py=[]
	for l in Ls:
		Px.append(l.P0[0])
		Py.append(l.P0[1])
		Px.append(l.P1[0])
		Py.append(l.P1[1])
	return Px,Py

hdelta=np.sqrt(1-1/4)
Px,Py=Fractal((-.5,-1*hdelta/3),8,1)

fig,ax=plt.subplots(figsize=(5,5))
ax.plot(Px,Py,linewidth=2/(1+2))

ax.set_xlim((0,.75))
ax.set_ylim((0,.75))
dx0=np.array([0,.75])
dy0=np.array([0,.75])
k=.75-.385
p=.31
dx1=np.array([0,k-k*p])
dy1=np.array([.75-k,.75-k*p])
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
for i in np.arange(0,1+1e-10,.02):
	dx=lerp(dx0,dx1,i)
	dy=lerp(dy0,dy1,i)
	ax.set_xlim((dx[0],dx[1]))
	ax.set_ylim((dy[0],dy[1]))

	ax.set_aspect("equal")
	plt.savefig(f"Fractal{int(np.round(i*100)):03d}_vid.png",dpi=200)


