#!/usr/bin/env python3

#
#    Dynamic system of population grow with limited resources
#    Copyright (C) 2022  Victor De la Luz
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

# x = ((1+rc)/r)*a

import matplotlib.pyplot as plt
import numpy as np

# a = rho*a*(1-a)

# rho = 1 + r*c
# x = ((1+rc)/r)*a

c=10
x0= 40.0/51.0
r=0.255

a0 = 0.2
rho = 3.55

fig, ax = plt.subplots()

a = a0
X = []
X.append(x0)

itera = np.arange(0,26)

for i in itera:
    a = rho*a*(1.0 - a)
    X.append(((1.0+ r*c)/r)*a)
    
ax.plot(X, linewidth=2.0)#,label='c='+str(c)  )


#r= 0.01
#c = 10





#itera = np.arange(0,1)
#c_range = np.arange(0,1,1)
#x0_range = np.arange(0,1,1)
#
#fig, ax = plt.subplots()
#
#
#for x0 in x0_range:
#    for c in c_range:
#        rho = 1.0 + r*c
#        X = []
#        X.append(x0)
#        a = (  (r / (1.0 + r*c))*x0  )
#
#        for i in itera:
#            a = rho*a*(1.0 - a)
#            X.append( ((1.0+ r*c)/r)*a  )
#
#        ax.plot(X, linewidth=2.0,label='c='+str(c)  )
#

#plt.yscale('log')
#plt.legend()
plt.title('a = rho*a*(1-a) periodic 4')
plt.savefig('population-grow-resources-periodic-four-cycle.png')
plt.show()
