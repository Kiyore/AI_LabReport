)import random

def generate_clauses(k, m, n):
    clauses = []
    variables = list(range(1, n + 1))
    for _ in range(m):
        clause = set()
        for _ in range(k):
            var = random.choice(variables)
            if random.choice([True, False]):
                clause.add(-var)
            else:
                clause.add(var)
        clauses.append(clause)
    return clauses
