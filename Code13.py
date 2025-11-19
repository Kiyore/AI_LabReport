import random
import itertools

def variable_neighborhood_search(num_variables, clauses, maxk):
    def fitness(sol):
        return sum(any(sol[abs(lit)-1] if lit > 0 else not sol[abs(lit)-1] for lit in clause) for clause in clauses)
    solution = [random.choice([True, False]) for _ in range(num_variables)]
    best_fitness = fitness(solution)
    improvement = True
    while improvement:
        improvement = False
        k = 1
        while k <= maxk:
            neighbors = []
            for indices in itertools.combinations(range(num_variables), k):
                neighbor = solution.copy()
                for i in indices:
                    neighbor[i] = not neighbor[i]
                neighbors.append(neighbor)
            neighbor_fitness = [fitness(n) for n in neighbors]
            best_idx = neighbor_fitness.index(max(neighbor_fitness))
            if neighbor_fitness[best_idx] > best_fitness:
                solution = neighbors[best_idx]
                best_fitness = neighbor_fitness[best_idx]
                improvement = True
                k = 1
            else:
                k += 1
    return solution, best_fitness

clauses = [[1, -2, 3], [-1, 2], [2, 3, -4]]
print(variable_neighborhood_search(4, clauses, 2))
