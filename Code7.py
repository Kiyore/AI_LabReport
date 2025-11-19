import heapq

def astarplagiarism(doc1, doc2, get_successors, editdistance, heuristic):
    startstate = (0, 0)
    goalstate = (len(doc1), len(doc2))
    openlist = []
    heapq.heappush(openlist, (0, 0, startstate, None))
    visited = set()
    parent = {}

    while openlist:
        f, g, state, parent_state = heapq.heappop(openlist)
        if state in visited:
            continue
        visited.add(state)
        parent[state] = parent_state

        if state == goalstate:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for successor in get_successors(state, doc1, doc2):
            idx1, idx2 = successor
            if idx1 < len(doc1) and idx2 < len(doc2):
                g_new = g + editdistance(doc1[idx1], doc2[idx2])
            else:
                g_new = g + 1
            h = heuristic(successor, doc1, doc2)
            f_new = g_new + h
            heapq.heappush(openlist, (f_new, g_new, successor, state))

    return None
