
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 3},
    'G': {}
}

h = {'A': 7, 'B': 6, 'C': 4, 'D': 4, 'E': 2, 'G': 0}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(h[start], 0, start, [start])]
visited = set()

while open_list:
    open_list.sort()
    f, g, node, path = open_list.pop(0)

    if node == goal:
        print("Shortest Path:", path)
        print("Total Cost:", g)
        break

    if node not in visited:
        visited.add(node)

        for next_node in graph[node]:
            if next_node not in visited:
                new_g = g + graph[node][next_node]
                new_f = new_g + h[next_node]
                open_list.append((new_f, new_g, next_node, path + [next_node]))
else:
    print("No path found")
