
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color = {}

def safe(region, c):
    for neighbor in graph[region]:
        if color.get(neighbor) == c:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for c in colors:
        if safe(region, c):
            color[region] = c

            if solve(regions[1:]):
                return True

            del color[region]

    return False

if solve(list(graph.keys())):
    print("Map Coloring:")
    for region in color:
        print(region, ":", color[region])
else:
    print("No solution exists")
