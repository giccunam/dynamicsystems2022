#!/usr/bin/env python3
import matplotlib.pyplot as plt


def insideTriangle(xp, yp, xA, yA, xB, yB, xC, yC, ax) :
    a = ((yB-yC) * (xp-xC) + (xC-xB) * (yp-yC)) / ((yB-yC) * (xA-xC) + (xC-xB) * (yA-yC))
    b = ((yC-yA) * (xp-xC) + (xA-xC) * (yp-yC)) / ((yC-yA) * (xB-xC) + (xA-xC) * (yB-yC))
    c = 1-a-b
    if (0<=a) and (a<=1) and (0<=b) and (b<=1) and (0<=c) and (c<=1) :
        ax.scatter(xp,yp, color = 'green')
        return True
    else :
        ax.scatter(xp,yp,color = 'red')
        return False

xA = 0
yA = 0
xB = 1
yB = 0
xC = 0
yC = 1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([xA,xB,xC,xA],[yA,yB,yC,yA])
ax.scatter(xA,yA, color = 'blue')
ax.scatter(xB,yB, color = 'blue')
ax.scatter(xC,yC, color = 'blue')

print(insideTriangle(0.25,0.25,0,0,1,0,0,1,ax))
print(insideTriangle(1,1,0,0,1,0,0,1,ax))

#print(insideTriangle(6,6,1,1,4,8,10,6,ax))
#print(insideTriangle(8,4,1,1,4,8,10,6,ax))


plt.show()
