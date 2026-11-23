import random

# Fitness function
def fitness(x):
    return x * x

# Initial population
population = [random.randint(0, 31) for i in range(6)]

# Genetic Algorithm
for generation in range(20):

    new_population = [max(population, key=fitness)]

    while len(new_population) < 6:
        p1 = max(random.sample(population, 2), key=fitness)
        p2 = max(random.sample(population, 2), key=fitness)

        b1 = format(p1, '05b')
        b2 = format(p2, '05b')

        point = random.randint(1, 4)

        c1 = int(b1[:point] + b2[point:], 2)
        c2 = int(b2[:point] + b1[point:], 2)

        for child in (c1, c2):
            if random.random() < 0.1:
                bit = random.randint(0, 4)
                child = child ^ (1 << bit)

            if len(new_population) < 6:
                new_population.append(child)

    population = new_population

best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))
