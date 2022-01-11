# We have a set of points described by (x, y) coordinates in the two dimensional space.
# Create a function, that calculates coordinates of smallest possible square (coord and size) that fits all of them.
# Two sides of the square are expected to be parallel to the x axis

import numpy as np

# N = 5
# x = np.random.rand(N)
# y = np.random.randint(N)
# x=100*x

# print(x," ")
xCo = []
yCo = []
a=6
b=6
points = [(4, 5), (8, 2),(1, 2), (3, 3)]
points.append((6,6))
print(points)
for x in points:
    xCo.append(x[0])
    yCo.append(x[1])
print(xCo)
print(yCo)

xCo.sort()
yCo.sort()
print(xCo)
print(yCo)

xDist = xCo[-1] - xCo[0]
print("X longest dist : ", xDist)
yDist = yCo[-1] - yCo[0]
print("Y longest dist : ", yDist)

if xDist > yDist:
    print("Square size is : ", xDist, " x ", xDist)
else:print("Square size is : ", yDist, " x ", yDist)
# x=points[1]
# x1=x[0]
# print(x)
# print(x1)
import matplotlib.pyplot as plt
for x in points:
    c,d= zip(x)
    plt.plot(c,d, marker="o", color="red")
plt.show()