import random

raagbhairavasc = ['C', 'C', 'E', 'F', 'G', 'G', 'B']
raagbhairavdesc = ['C', 'B', 'G', 'G', 'F', 'E', 'C']

def mutate(melody, mutation_rate):
    for i in range(len(melody)):
        if random.random() < mutation_rate:
            melody[i] = random.choice(random.choice([raagbhairavasc, raagbhairavdesc]))
    return melody

def fitness(melody):
    return sum(1 for i in range(len(melody)-1) if melody[i] == melody[i+1])

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    return parent1[:point] + parent2[point:]

def genetic_algorithm(generations, population_size, mutation_rate, melody_length):
    population = [[random.choice(raagbhairavasc) for _ in range(melody_length)] for _ in range(population_size)]
    for _ in range(generations):
        scored = [(melody, fitness(melody)) for melody in population]
        scored.sort(key=lambda x: x[1], reverse=True)
        population = [melody for melody, _ in scored[:population_size//2]]
        new_population = []
        while len(new_population) < population_size:
            parents = random.sample(population, 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best = max(population, key=fitness)
    return best

print(genetic_algorithm(50, 10, 0.2, 7))
