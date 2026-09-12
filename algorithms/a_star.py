from heapq import heappop, heappush


def a_star(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]) -> int:
    """
    Returns the shortest path cost from start to goal.

    grid:
        0 -> free cell
        1 -> blocked cell

    BFS -> priority = nº of steps
    Dijkstra -> priority = g(n)
    A* -> priority = g(n) + h(n)

    Structure:

    heap = [(h(start), 0, start)]

    while heap:
        pop smallest f

        if goal:
            return

            for neighbour:
                tentative_g = current_g + cost

                if better:
                    update g
                    f = g + h
                    push

    > When does A guarantee the optimal path?
    < When the heuristic is admissible, meaning it never overestimates the true remaining cost.
    """
    rows, cols = len(grid), len(grid[0])

    def heuristic(node: tuple[int, int]) -> int:
        row, col = node
        goal_row, goal_col = goal

        # Euclidean distance
        # return (goal_row - row) ** 2 + (goal_col - col) ** 2

        # Manhattan distance
        return abs(goal_row - row) + abs(goal_col - col)

    def is_valid(row: int, col: int) -> bool:
        # We check if the cell is free and in-bounds
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0

    g_row, g_col = goal
    s_row, s_col = start
    if not is_valid(g_row, g_col) or not is_valid(s_row, s_col):
        return -1

    # (f_score, g_score, node)
    min_heap: list[tuple[int, int, tuple[int, int]]] = [(heuristic(start), 0, start)]

    # Memoized distances from start to some point
    g_score: dict[tuple[int, int], int] = {start: 0}

    directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while min_heap:
        _, current_g, current_node = heappop(min_heap)

        # Base case
        if current_node == goal:
            return current_g

        row, col = current_node

        for dir_row, dir_col in directions:
            new_row = row + dir_row
            new_col = col + dir_col

            # Always check if the new node path is in bounds
            if not is_valid(new_row, new_col):
                continue

            neighbour: tuple[int, int] = (new_row, new_col)

            # Each move costs 1 unit in this case of grid
            tentative_g: int = current_g + 1

            if tentative_g < g_score.get(neighbour, float("inf")):
                # Update with the new best score for the path
                g_score[neighbour] = tentative_g

                # We need to know which is the scored distance towards the goal
                f_score: int = tentative_g + heuristic(neighbour)

                heappush(min_heap, (f_score, tentative_g, neighbour))

    return -1


if __name__ == "__main__":
    # Example
    grid: list[list[int]] = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start: tuple[int, int] = (0, 0)
    goal: tuple[int, int] = (4, 4)

    print(
        f"The shortest path cost from {start} to {goal} is: {a_star(grid, start, goal)}"
    )
    print(
        f"The shortest path cost from {(0,0)} to {(2,3)} is: {a_star(grid, (0,0), (2,3))}"
    )
