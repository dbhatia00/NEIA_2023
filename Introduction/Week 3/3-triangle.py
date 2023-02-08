# A program to determine which triangle is largest
# Using lists and conditionals!

import math

points = []
sub_points_list = []

x = float(input("Enter p1's x: "))
y = float(input("Enter p1's y: "))
sub_points_list.append(x)
sub_points_list.append(y)
points.append(sub_points_list)
sub_points_list = []

x = float(input("Enter p2's x: "))
y = float(input("Enter p2's y: "))
sub_points_list.append(x)
sub_points_list.append(y)
points.append(sub_points_list)
sub_points_list = []

x = float(input("Enter p3's x: "))
y = float(input("Enter p3's y: "))
sub_points_list.append(x)
sub_points_list.append(y)
points.append(sub_points_list)
sub_points_list = []

print(points)

areas = []
areas.append(points[0][0] * points[0][1] * 0.5)
areas.append(points[1][0] * points[1][1] * 0.5)
areas.append(points[2][0] * points[2][1] * 0.5)

if (areas[0] > areas[1] and areas[0] > areas[2]):
    print(areas[0])
elif(areas[1] > areas[0] and areas[1] > areas[2]):
    print(areas[1])
else:
    print(areas[2])
