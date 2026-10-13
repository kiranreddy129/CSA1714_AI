
n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input("Enter node: ")
    graph[node] = input("Enter adjacent nodes: ").split()

start = input("Enter starting node: ")

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for x in graph[node]:
            dfs(x)

print("DFS Traversal:")
dfs(start)
