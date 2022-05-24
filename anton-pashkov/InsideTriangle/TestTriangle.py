#/usr/bin/env python3
import InsideTriangle as it
import matplotlib.pyplot as plt

x1_a, y1_a, x2_a, y2_a, x3_a, y3_a = 0, 0, 5, 2, 2, 7

tris = [[0, 0, 5, 2, 2, 7]]

points = [[2, 2], [4, 1], [5, 4], [0, 3], [4, 6], [1, 3]]

for t in tris:
    for p in points:
        res = it.insideTriangle(p[0], p[1], t[0], t[1], t[2], t[3], t[4], t[5])
        if res == True:
            plt.scatter(p[0], p[1], c='green')
            print(f'{p} is in {t}')
        else:
            plt.scatter(p[0], p[1], c='red')
            print(f'{p} is not in {t}')

plt.plot([0, 5, 2, 0], [0, 2, 7, 0])
plt.show()
