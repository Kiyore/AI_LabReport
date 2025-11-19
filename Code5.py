def find_path_dfs(initial_state, goal_state, get_moves, apply_move):
    stack = [(initial_state, [initial_state])]
    visited = set([initial_state])
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path
        for move in get_moves(current_state):
            new_state = apply_move(current_state, move)
            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [new_state]))
    return "No solution found"
