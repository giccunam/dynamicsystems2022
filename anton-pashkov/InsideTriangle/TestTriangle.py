import InsideTriangle as it
import matplotlib.pyplot as plt

x1_a, y1_a, x2_a, y2_a, x3_a, y3_a = 0, 0, 5, 2, 2, 7

tris = [[0, 0, 5, 2, 2, 7], [6, 0, 2, 3, 7, 7], [1, 6, 3, 4, -1, 2]]

points = [[2, 2], [4, 1], [5, 4], [0, 3], [4, 6], [1, 3]]

for t in tris:
    for p in points:
        res = it.insideTriangle(p[0], p[1], t[0], t[1], t[2], t[3], t[4], t[5])
        if res == True:
            print(f'{p} is in {t}')
        else:
            print(f'{p} is not in {t}')

plt.plot([0, 5, 2, 0], [0, 2, 7, 0])
plt.plot([6, 2, 7, 6], [0, 3, 7, 0])
plt.plot([1, 3, -1, 1], [6, 4, 2, 6])
plt.scatter([2, 4, 5, 0, 4, 1], [2, 1, 4, 3, 6, 3])
plt.show()
