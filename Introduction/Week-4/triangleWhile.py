# A program to determine which triangle is largest
# Using lists and conditionals!

import math
from triangleFor import getUserInput
from triangleFor import calcArea


points = []
areas = []
continueAsking = input('Would you like to enter points to be evaluated? (y/n) ')
numTriangles = 0
while continueAsking == 'y':
    # USE getUserInput() TO GET THE POINTS
    points = getUserInput('Enter p' + str(numTriangles), points)
    # USE calcArea() TO CALCULATE AREAS
    areas.append(calcArea(points[numTriangles][0], points[numTriangles][1]))

    numTriangles +=1
    continueAsking = input('You have entered ' + str(numTriangles) + ' triangle(s), enter another? (y/n) ')

if numTriangles != 0:
    maxTriangle = areas.index(max(areas))
    print("Triangle " + str(maxTriangle) + " is the largest with points " + str(points[maxTriangle]))