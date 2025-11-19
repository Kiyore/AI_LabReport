import random

def hill_climbing(num_variables, clauses):
    solution = [random.choice([True, False]) for _ in range(num_variables)]
    def fitness(sol):
        return sum(any(sol[abs(lit)-1] if lit > 0 else not sol[abs(lit)-1] for lit in clause) for clause in clauses)
    current_fitness = fitness(solution)
    while True:
        neighbors = []
        for i in range(num_variables):
            neighbor = solution.copy()
            neighbor[i] = not neighbor[i]
            neighbors.append(neighbor)
        neighbor_fitness = [fitness(n) for n in neighbors]
        best_idx = neighbor_fitness.index(max(neighbor_fitness))
        if neighbor_fitness[best_idx] > current_fitness:
            solution = neighbors[best_idx]
            current_fitness = neighbor_fitness[best_idx]
        else:
            break
    return solution, current_fitness

clauses = [[1, -2, 3], [-1, 2], [2, 3, -4]]
print(hill_climbing(4, clauses))

