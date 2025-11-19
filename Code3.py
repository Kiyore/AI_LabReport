 def generate_states():
    state = 'EEEWWW'
    states = [state]
    visited = set([state])
    for s in states:
        for move in get_possible_moves(s):
            new_state = perform_move(s, move)
            if new_state not in visited:
                visited.add(new_state)
                states.append(new_state)
    return states
