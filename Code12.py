import random

def beam_search(num_variables, clauses, beam_width):
    def fitness(sol):
        return sum(any(sol[abs(lit)-1] if lit > 0 else not sol[abs(lit)-1] for lit in clause) for clause in clauses)
    beam = [[random.choice([True, False]) for _ in range(num_variables)] for _ in range(beam_width)]
    best_fitness = max(fitness(sol) for sol in beam)
    while True:
        neighbors = []
        for sol in beam:
            for i in range(num_variables):
                neighbor = sol.copy()
                neighbor[i] = not neighbor[i]
                neighbors.append(neighbor)
        ranked = sorted(neighbors, key=fitness, reverse=True)
        new_beam = ranked[:beam_width]
        new_best_fitness = fitness(new_beam[0])
        if new_best_fitness <= best_fitness:
            break
        beam = new_beam
        best_fitness = new_best_fitness
    return new_beam[0], best_fitness

clauses = [[1, -2, 3], [-1, 2], [2, 3, -4]]
print(beam_search(4, clauses, 3))
