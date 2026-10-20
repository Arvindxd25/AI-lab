""" Assignment 5 - Blocks World using BFS """

# Blocks World: BFS finds a sequence of legal block moves
from collections import deque

# Each pile is written from bottom block to top block
start = (("A",), ("B",), ("C",))
goal_pile = ("C", "B", "A")

def is_goal(state):
    return goal_pile in state

def get_moves(state):
    new_states = []

    for source in range(3):
        if not state[source]:
            continue

        block = state[source][-1]  # only the top block can move
        source_pile = state[source][:-1]

        for destination in range(3):
            if source == destination:
                continue

            new_state = list(state)
            new_state[source] = source_pile
            new_state[destination] = state[destination] + (block,)
            new_states.append(tuple(new_state))

    return new_states

queue = deque([(start, [start])])
visited = {start}
answer = None

while queue:
    state, path = queue.popleft()

    if is_goal(state):
        answer = path
        break

    for next_state in get_moves(state):
        if next_state not in visited:
            visited.add(next_state)
            queue.append((next_state, path + [next_state]))

if answer:
    for step, state in enumerate(answer):
        print("Step", step, ":", state)
else:
    print("No solution found.")
