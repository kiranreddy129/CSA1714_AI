data = [
    [1, 2, 0],
    [2, 3, 0],
    [3, 3, 0],
    [6, 7, 1],
    [7, 8, 1],
    [8, 7, 1]
]

x = float(input("Enter first value: "))
y = float(input("Enter second value: "))

distance_a = 999
distance_b = 999

for point in data:
    d = (point[0] - x)**2 + (point[1] - y)**2

    if point[2] == 0 and d < distance_a:
        distance_a = d
    elif point[2] == 1 and d < distance_b:
        distance_b = d

if distance_a < distance_b:
    print("Predicted Class: A")
else:
    print("Predicted Class: B")
