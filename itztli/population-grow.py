#!/usr/bin/env python3

#
#    Dynamic system of population grow
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

import matplotlib.pyplot as plt

print("x = ( 1 + r ) x")

x0 = 2
r = 0.1
X = []
X.append(x0)
x = x0

for i in range(100):
    x = ( 1.0 + r )*x
    X.append(x)
    
fig, ax = plt.subplots()

ax.plot(X, linewidth=2.0,label='x0='+str(x0)+' r='+str(r)  )
plt.yscale('log')
plt.legend()
plt.title('x = (1+r)x')
plt.savefig('population-grow.png')
plt.show()

