from collections import deque

def safe(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if 3 - m > 0 and 3 - m < 3 - c:
        return False
    return True

start = (3, 3, 1)
goal = (0, 0, 0)

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        print("Solution:")
        for s in path + [state]:
            print(s)
        break

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for x, y in moves:
        if boat == 1:
            new_state = (m - x, c - y, 0)
        else:
            new_state = (m + x, c + y, 1)

        if new_state not in visited and safe(new_state[0], new_state[1]):
            visited.add(new_state)
            queue.append((new_state, path + [state]))
else:
    print("No solution")
