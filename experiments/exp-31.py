import math

data = [
    [1, 2, 'A'],
    [2, 3, 'A'],
    [3, 3, 'A'],
    [6, 7, 'B'],
    [7, 8, 'B'],
    [8, 7, 'B']
]

k = 3

x = float(input("Enter X value: "))
y = float(input("Enter Y value: "))

distances = []

for point in data:
    d = math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
    distances.append((d, point[2]))

distances.sort()
neighbors = distances[:k]

count_a = 0
count_b = 0

for neighbor in neighbors:
    if neighbor[1] == 'A':
        count_a += 1
    else:
        count_b += 1

if count_a > count_b:
    print("Predicted Class: A")
else:
    print("Predicted Class: B")
