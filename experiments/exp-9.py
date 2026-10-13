
n = int(input("Enter number of cities: "))
cost = []

print("Enter cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

start = 0
visited = [False] * n
visited[start] = True
path = [start]
total = 0
current = start

while len(path) < n:
    next_city = -1
    minimum = float('inf')

    for i in range(n):
        if not visited[i] and cost[current][i] < minimum:
            minimum = cost[current][i]
            next_city = i

    current = next_city
    visited[current] = True
    path.append(current)
    total += minimum

total += cost[current][start]
path.append(start)

print("Tour:", path)
print("Total Cost:", total)
