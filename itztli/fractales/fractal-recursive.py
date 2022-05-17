#!/usr/bin/env python3
#
#
#    vdelaluz@enesmorelia.unam.mx
#    Copyright (C) 2022 Victor De la Luz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import numpy as np
import math
import matplotlib.pyplot as plt

def triangle(x,y,mu,l,s):
    theta = np.arctan(mu)
    n = s*math.sqrt(l*l - math.pow(l/2.0,2))
    Q1 = [(x-(l/2.0)*math.cos(theta)),(y-(l/2.0)*math.sin(theta))]
    Q2 = [(x+(l/2.0)*math.cos(theta)),(y+(l/2.0)*math.sin(theta))]
    Q3 = [(x-n*math.sin(theta)),(y+n*math.cos(theta))]
    return [Q1[0],Q2[0],Q3[0],Q1[0] ] , [Q1[1],Q2[1],Q3[1],Q1[1]]

def computeCoordinates(x, y, l, mu, x_Q1, y_Q1, x_Q2, y_Q2, x_Q3, y_Q3):
    l1 = l / 3.0
    m1 = (y_Q3 - y_Q1)/(x_Q3 - x_Q1)
    m2 = (y_Q3 - y_Q2)/(x_Q3 - x_Q2)
    m3 = mu
    x_r1= (x_Q1+x_Q3)*0.5
    y_r1= (y_Q1+y_Q3)*0.5
    x_r2= (x_Q3+x_Q2)*0.5
    y_r2= (y_Q3+y_Q2)*0.5
    x_r3= x
    y_r3= y
    return l1, m1,m2,m3, x_r1, y_r1, x_r2, y_r2, x_r3, y_r3 

def fractal(n, ax, x, y, mu, l):
    if n > 0:
        X, Y = triangle(x,y,mu,l,1)
        ax.plot(X,Y)
        l1,m1,m2,m3,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3=computeCoordinates(x,y,l,mu,X[0], Y[0], X[1], Y[1], X[2], Y[2])
        fractal(n-1,ax, x_r1, y_r1,m1,l1)
        fractal(n-1,ax, x_r2, y_r2,m2,l1)
        fractal(n-1,ax, x_r3, y_r3,m3,l1)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

#P0
x=0.0
y=0.0
mu=0.0
l=1.0

fractal(6, ax, x, y, mu, l)

#
#
#X, Y = triangle(x,y,mu,l,1)
#ax.plot(X,Y)
#l1,m1,m2,m3,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3=computeCoordinates(x,y,l,mu,X[0], Y[0], X[1], Y[1], X[2], Y[2])
#
#ax.scatter(x_r1,y_r1)
#ax.scatter(x_r2,y_r2)
#ax.scatter(x_r3,y_r3)
#
#X, Y = triangle(x_r1,y_r1,m1,l1,1)
#ax.plot(X,Y)
#
#X, Y = triangle(x_r2,y_r2,m2,l1,1)
#ax.plot(X,Y)
#
#X, Y = triangle(x_r3,y_r3,m3,l1,-1)
#ax.plot(X,Y)

plt.show()
