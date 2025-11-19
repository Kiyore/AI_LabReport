from collections import deque

def find_path(initial_state, goal_state, get_moves, apply_move):
    queue = deque([(initial_state, [initial_state])])
    visited = set([initial_state])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        for move in get_moves(current_state):
            new_state = apply_move(current_state, move)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
    return "No solution found"
