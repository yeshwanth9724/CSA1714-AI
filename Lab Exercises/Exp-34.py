import random

def fitness(x):
    return x * x

random.seed(42)
population = [random.randint(0, 10) for _ in range(5)]

for i in range(10):
    population.sort(key=fitness, reverse=True)

    parent1 = population[0]
    parent2 = population[1]

    child = (parent1 + parent2) // 2
    population[-1] = child

best = max(population, key=fitness)

print("Genetic Algorithm Optimization")
print("Best value of x:", best)
print("Maximum value:", fitness(best))
