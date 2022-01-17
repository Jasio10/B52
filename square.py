# We have a set of points described by (x, y) coordinates in the two dimensional space.
# Create a function, that calculates coordinates of the smallest possible square (coord and size) that fits all of them.
# Two sides of the square are expected to be parallel to the x-axis
# Program prints results on console and draws points and square in a separate window

import json
import argparse
import matplotlib.pyplot as plt

xCo = []
yCo = []

# Uploading points from JSON file
def read_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", required=True, type=str)
    file_name = parser.parse_args()
    return file_name

def read_points(file_name):
    try:
        f_n = file_name.filename
        if not f_n.endswith('.json'):
            print("File is not JSON file ")
            exit()
#        f = open(file_name.filename)
        with open(file_name.filename) as json_data:
            points = json.load(json_data)
        for x in points:
            if len(x) != 2:
                print("\nPoint needs two coordinates only, NOT: ", x)
                exit()
    except IOError:
        print('File:', file_name.filename,' not found')
        exit()
    except ValueError:
        print('Expecting numerical data in format : [[x,y], [x,y], ...]')
        f = open(file_name.filename)
        print("Content of file is : ", f.read())
        exit()
    print("Points from file : ", points)
    return points


# Calculating smallest possible square that fits all points
def calc_square(points):

    for x in points:
        xCo.append(x[0])
        yCo.append(x[1])
    xCo.sort()
    yCo.sort()

    xDist = xCo[-1] - xCo[0]
    yDist = yCo[-1] - yCo[0]

    if xDist > yDist:
        dist = xDist
        print("\nSquare size is : ", dist, " x ", dist)
    else:
        dist = yDist
        print("Smallest square size is : ", dist, " x ", dist)
    return dist

# Generating corners of the smallest square
def square_corners(dist):
    firstPt = (xCo[0], yCo[0])
    secondPt = (firstPt[0] + dist, firstPt[1])
    thirdPt = (secondPt[0], secondPt[1] + dist)
    fourthPt = (thirdPt[0] - dist, thirdPt[1])
    squarePt = []
    squarePt.append(firstPt)
    squarePt.append(secondPt)
    squarePt.append(thirdPt)
    squarePt.append(fourthPt)
    print("Four corners of the smallest square : ", squarePt)
    return squarePt, firstPt

# Drawing square and points
def drawing_sq(squarePt, firstPt):
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

file_name = read_file_name()
points = read_points(file_name)
dist = calc_square(points)
squarePt, firstPt = square_corners(dist)
drawing_sq(squarePt, firstPt)