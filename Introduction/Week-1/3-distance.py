# A program to calculate the distance between two points

# Assume p1 = (10, 10) and p2 = (0, 0)

import math

x1 = 3
x2 = 0

y1 = 4
y2 = 0

x_block = (x2 - x1) ** 2
y_block = (y2 - y1) ** 2

print(math.sqrt(x_block + y_block))