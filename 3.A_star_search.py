""" Assignment 3 - A* Search for 8-Puzzle """

# A* search using the number of misplaced tiles
import heapq

# 0 represents the empty space
start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_next_states(state):
    empty = state.index(0)
    row, col = divmod(empty, 3)
    next_states = []

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_empty = r * 3 + c
            new_state = list(state)
            new_state[empty], new_state[new_empty] = new_state[new_empty], new_state[empty]
            next_states.append(tuple(new_state))

    return next_states

def a_star():
    open_list = [(heuristic(start), 0, start, [start])]
    best_cost = {start: 0}

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path

        for next_state in get_next_states(state):
            new_g = g + 1

            if new_g < best_cost.get(next_state, float("inf")):
                best_cost[next_state] = new_g
                new_f = new_g + heuristic(next_state)
                heapq.heappush(
                    open_list, (new_f, new_g, next_state, path + [next_state])
                )

    return None

answer = a_star()

if answer:
    print("Minimum moves:", len(answer) - 1)
    for state in answer:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found.")
