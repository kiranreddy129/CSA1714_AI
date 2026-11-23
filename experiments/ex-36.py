import math

data = [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]

mean_x = sum(row[0] for row in data) / len(data)
mean_y = sum(row[1] for row in data) / len(data)

a = 0
b = 0
d = 0

for row in data:
    x = row[0] - mean_x
    y = row[1] - mean_y
    a += x * x
    b += x * y
    d += y * y

angle = 0.5 * math.atan2(2 * b, a - d)

print("Original Data:")
for row in data:
    print(row)

print("Reduced Data:")
for row in data:
    x = row[0] - mean_x
    y = row[1] - mean_y
    reduced = x * math.cos(angle) + y * math.sin(angle)
    print(round(reduced, 2))
