graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [start]
visited = []

while open_list:
    open_list.sort(key=lambda x: h[x])
    node = open_list.pop(0)

    if node not in visited:
        print("Visited:", node)
        visited.append(node)

        if node == goal:
            print("Goal Found!")
            break

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                open_list.append(neighbor)
else:
    print("Goal not found")
