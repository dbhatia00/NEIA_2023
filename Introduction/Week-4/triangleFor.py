# A program to determine which triangle is largest
# Using lists and conditionals!

import math

def getUserInput(inputString, points):
    sub_points_list = []
    x = float(input(inputString + ' x: '))
    y = float(input(inputString + ' y: '))
    sub_points_list.append(x)
    sub_points_list.append(y)
    points.append(sub_points_list)
    return points

def calcArea(val1, val2):
    return val1 * val2 * 0.5

def handleBadInput(badInput):
    while (badInput != 'y') and (badInput != 'n'):
        badInput = input('Bad input, enter y or n - ')
    return badInput 

def main():
    points = []
    num_triangles = int(input('Enter num triangles: '))

    for i in range(0, num_triangles):
        points = getUserInput('Enter p' + str(i), points)

    areas = []
    for i in range(0, num_triangles):
        areas.append(calcArea(points[i][0], points[i][1]))

    print("Triangle " + str(areas.index(max(areas))) + " is the largest")