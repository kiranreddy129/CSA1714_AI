import random

weights = [2, 3, 4, 5, 6]
values = [3, 4, 5, 6, 7]
capacity = 10

population = []

for i in range(6):
    population.append([random.randint(0, 1) for j in range(5)])

for generation in range(20):
    fitness = []

    for chromosome in population:
        weight = 0
        value = 0

        for i in range(5):
            if chromosome[i] == 1:
                weight += weights[i]
                value += values[i]

        if weight <= capacity:
            fitness.append(value)
        else:
            fitness.append(0)

    new_population = []

    for i in range(6):
        p1 = population[fitness.index(max(fitness))]
        p2 = random.choice(population)

        child = p1[:3] + p2[3:]

        if random.random() < 0.2:
            pos = random.randint(0, 4)
            child[pos] = 1 - child[pos]

        new_population.append(child)

    population = new_population

best = max(population, key=lambda c: sum(values[i] for i in range(5) if c[i] == 1)
           if sum(weights[i] for i in range(5) if c[i] == 1) <= capacity else 0)

total_weight = sum(weights[i] for i in range(5) if best[i] == 1)
total_value = sum(values[i] for i in range(5) if best[i] == 1)

print("Selected Items:", best)
print("Total Weight:", total_weight)
print("Total Value:", total_value)
