from collections import deque

n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    graph[node] = input("Enter adjacent nodes: ").split()

start = input("Enter starting node: ")

queue = deque([start])
visited = [start]

print("BFS Traversal:")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for x in graph[node]:
        if x not in visited:
            visited.append(x)
            queue.append(x)
