import math

x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2): ").split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")