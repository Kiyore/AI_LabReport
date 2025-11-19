import heapq

def astar(startstate, goalstate, get_successors, manhattan_distance):
    openlist = []
    heapq.heappush(openlist, (manhattan_distance(startstate, goalstate), 0, startstate, None))
    visited = set()
    nodesexplored = 0
    parent = {}

    while openlist:
        f, g, currentstate, parent_state = heapq.heappop(openlist)
        if currentstate in visited:
            continue
        visited.add(currentstate)
        parent[currentstate] = parent_state
        nodesexplored += 1

        if currentstate == goalstate:
            path = []
            while currentstate is not None:
                path.append(currentstate)
                currentstate = parent[currentstate]
            return path[::-1], nodesexplored

        for successor in get_successors(currentstate):
            if successor not in visited:
                g_new = g + 1
                h = manhattan_distance(successor, goalstate)
                heapq.heappush(openlist, (g_new + h, g_new, successor, currentstate))

    return "Failure", nodesexplored
