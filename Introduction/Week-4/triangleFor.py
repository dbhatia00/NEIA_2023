# A program to determine which triangle is largest
# Using lists and conditionals!

import math

def getUserInput(inputString, points):
    sub_points_list = []
    x = float(input(inputString))
    y = float(input(inputString))
    sub_points_list.append(x)
    sub_points_list.append(y)
    points.append(sub_points_list)
    return points

def calcArea(val1, val2):
    return val1 * val2 * 0.5

points = []
sub_points_list = []

num_triangles = int(input('Enter num triangles: '))

for i in range(0, num_triangles):
    points = getUserInput('Enter p ', points)


print(points)

areas = []
for i in range(0, num_triangles):
    areas.append(calcArea(points[i][0], points[i][1]))


print(max(areas))
