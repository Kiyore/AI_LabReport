)import random
import math

def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))

def simulated_annealing(dist_matrix, temperature, stopping_temp, cooling_rate):
    n = len(dist_matrix)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    best_tour = current_tour[:]
    while temperature > stopping_temp:
        i, j = sorted(random.sample(range(n), 2))
        new_tour = current_tour[:]
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
        current_distance = total_distance(current_tour, dist_matrix)
        new_distance = total_distance(new_tour, dist_matrix)
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour
            if new_distance < total_distance(best_tour, dist_matrix):
                best_tour = new_tour
        temperature *= cooling_rate
    return best_tour, total_distance(best_tour, dist_matrix)

dist_matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
print(simulated_annealing(dist_matrix, 1000, 1, 0.99))
