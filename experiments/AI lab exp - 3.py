from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        print(jug1, jug2)

        if jug1 == target or jug2 == target:
            print("Target achieved!")
            return

        states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0)
        ]

        amount = min(jug1, capacity2 - jug2)
        states.append((jug1 - amount, jug2 + amount))

        amount = min(jug2, capacity1 - jug1)
        states.append((jug1 + amount, jug2 - amount))

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Target cannot be achieved.")


# 4-litre jug, 3-litre jug, target = 2 litres
water_jug(4, 3, 2)
