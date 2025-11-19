from collections import deque

def bfs(startstate, goalstate, get_successors):
    queue = deque([(startstate, [startstate])])
    visited = set()
    while queue:
        currentstate, path = queue.popleft()
        if currentstate == goalstate:
            return path
        if currentstate not in visited:
            visited.add(currentstate)
            for successor in get_successors(currentstate):
                if successor not in visited:
                    queue.append((successor, path + [successor]))
    return "No solution found"
