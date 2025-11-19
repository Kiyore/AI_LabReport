 def dfs(startstate, goalstate, get_successors):
    stack = [(startstate, [startstate])]
    visited = set()
    while stack:
        currentstate, path = stack.pop()
        if currentstate == goalstate:
            return path
        if currentstate not in visited:
            visited.add(currentstate)
            for successor in get_successors(currentstate):
                if successor not in visited:
                    stack.append((successor, path + [successor]))
    return "No solution found"
