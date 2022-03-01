#!/usr/bin/env python3
#
#    Example of dynamic system
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


print('Test 1 x = x + 1')

N=100
# plot
fig, ax = plt.subplots()

for x0 in range(1):
    for a in range (1):
        for b in range(5):
            X=[]
            x = x0+1 #initial condition 
            X.append(x)
            for i in range(N):
                x = (1/(b+1))*x + (a+1)
                X.append(x)
            ax.plot(X, linewidth=2.0,label='x0='+str(x0+1)+' a='+str(a+1)+' b='+str(1/(b+1)))
plt.legend()
plt.title('x = bx + a')
plt.show()

