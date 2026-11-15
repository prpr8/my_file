
import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Calculate Manhattan distance
def heuristic(state):
    h = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1

            r1, c1 = divmod(i, 3)   #divmod returns the quotient and remainder when dividing two numbers. In this case, it is used to calculate the row and column indices of the current position (i) in a 3x3 grid.
            r2, c2 = divmod(goal_pos, 3)

            h += abs(r1 - r2) + abs(c1 - c2)

    return h


# A* Search
def astar(start):

    pq = [(heuristic(start), 0, start)]

    cost = {start: 0}
    parent = {start: None}

    while pq:

        f, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        zero = state.index(0)
        r, c = divmod(zero, 3)

        moves = [(-1, 0), (1, 0),
                 (0, -1), (0, 1)]

        for dr, dc in moves:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:

                new_pos = nr * 3 + nc

                new_state = list(state)

                new_state[zero], new_state[new_pos] = \
                    new_state[new_pos], new_state[zero]

                new_state = tuple(new_state)

                new_cost = g + 1

                if new_cost < cost.get(new_state, 999):

                    cost[new_state] = new_cost
                    parent[new_state] = state

                    f = new_cost + heuristic(new_state)

                    heapq.heappush(
                        pq, (f, new_cost, new_state)
                    )

    return None


# Main program
path = astar(start)

if path:
    print("Number of moves:", len(path) - 1)
    print("Solution found:")

    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution")
