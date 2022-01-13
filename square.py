# We have a set of points described by (x, y) coordinates in the two dimensional space.
# Create a function, that calculates coordinates of the smallest possible square (coord and size) that fits all of them.
# Two sides of the square are expected to be parallel to the x-axis
# Program prints results on console and draws points and square in a separate window

import json
import argparse
import matplotlib.pyplot as plt

# Uploading points from JSON file
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", required=True, type=str)
args = parser.parse_args()
with open(args.filename) as json_data:
    points = json.load(json_data)
    print("Points from file : ", points)

# Calculating smallest possible square that fits all points
xCo = []
yCo = []
for x in points:
    xCo.append(x[0])
    yCo.append(x[1])
xCo.sort()
yCo.sort()
xDist = xCo[-1] - xCo[0]
yDist = yCo[-1] - yCo[0]

if xDist > yDist:
    Dist = xDist
    print("\nSquare size is : ", Dist, " x ", Dist)
else:
    Dist = yDist
    print("Smallest square size is : ", Dist, " x ", Dist)

# Generating corners of the smallest square
firstPt = (xCo[0], yCo[0])
secondPt = (firstPt[0]+Dist, firstPt[1])
thirdPt = (secondPt[0], secondPt[1]+Dist)
fourthPt = (thirdPt[0]-Dist, thirdPt[1])
squarePt = []
squarePt.append(firstPt)
squarePt.append(secondPt)
squarePt.append(thirdPt)
squarePt.append(fourthPt)
print("Four corners of the smallest square : ", squarePt)

# Drawing square and points
xCor = []
yCor = []
for x in squarePt:
    xCor.append(x[0])
    yCor.append(x[1])
xCor.append(firstPt[0])
yCor.append(firstPt[1])
plt.title("Smallest possible square that fits all points")
plt.plot(xCor, yCor)
for x in points:
    c, d = zip(x)
    plt.plot(c, d, marker="o", color="red")
plt.show()
