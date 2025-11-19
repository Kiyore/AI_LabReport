import heapq

def BestFS(startstate, goalstate, get_successors, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic(startstate, goalstate), startstate))
    explored = set()
    Totalnodesexpanded = 0

    while True:
        if not frontier:
            return None, Totalnodesexpanded
        h, current = heapq.heappop(frontier)
        if current in explored:
            continue
        explored.add(current)
        Totalnodesexpanded += 1
        if current == goalstate:
            return current, Totalnodesexpanded
        for child in get_successors(current):
            if child not in explored:
                heapq.heappush(frontier, (heuristic(child, goalstate), child))
