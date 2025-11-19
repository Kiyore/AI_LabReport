import heapq

def astarsearch(startstate, goalstate, findsuccessors, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic(startstate, goalstate), 0, startstate))
    explored = set()

    while frontier:
        f, g, current = heapq.heappop(frontier)
        if current == goalstate:
            return current
        explored.add(current)
        for successor in findsuccessors(current):
            if successor not in explored:
                g_new = g + 1
                h = heuristic(successor, goalstate)
                f_new = g_new + h
                heapq.heappush(frontier, (f_new, g_new, successor))
    return None

