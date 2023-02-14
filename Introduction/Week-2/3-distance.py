# A program to calculate the distance between two points
# With user input!

import math

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

x_block = (x2 - x1) ** 2
y_block = (y2 - y1) ** 2

print(math.sqrt(x_block + y_block))