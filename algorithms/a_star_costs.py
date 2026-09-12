from heapq import heappop, heappush


def a_star(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]) -> int:
    """
    Return the minimum path cost from start to goal.

    0 -> blocked cell
    n -> movement cost [whe n > 0]

    A* priority:
        f(n) = g(n) + h(n)
    where:
        g(n) = Real accumulated cost from start to n
        h(n) = estimated remaining cost from n to goal
    """
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    start_row, start_col = start
    goal_row, goal_col = goal

    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] > 0

    if not is_valid(start_row, start_col) or not is_valid(goal_row, goal_col):
        return -1

    # Minimum possible movement cost: used to keep the heuristic admissible.
    min_cost: int = min(cell for row in grid for cell in row if cell > 0)

    def heuristic(node: tuple[int, int]) -> int:
        row, col = node
        manhattan_distance: int = abs(goal_row - row) + abs(goal_col - col)
        return manhattan_distance * min_cost

    # (f_score, g_score, node)
    min_heap: list[tuple[int, int, tuple[int, int]]] = [(heuristic(start), 0, start)]

    # Best know real cost from start to some point (g_score)
    distances: dict[tuple[int, int], int] = {start: 0}
    directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while min_heap:
        _, current_distance, current_node = heappop(min_heap)

        if current_node == goal:
            return current_distance

        # Skip larger ditances
        if current_distance > distances.get(current_node, float("inf")):
            continue

        row, col = current_node

        for dir_row, dir_col in directions:
            new_row, new_col = row + dir_row, col + dir_col

            if not is_valid(new_row, new_col):
                continue

            neighbour: tuple[int, int] = (new_row, new_col)
            new_distance: int = current_distance + grid[new_row][new_col]

            if new_distance < distances.get(neighbour, float("inf")):
                distances[neighbour] = new_distance

                new_heuristic_distance: int = heuristic(neighbour) + new_distance
                heappush(min_heap, (new_heuristic_distance, new_distance, neighbour))

    return -1


if __name__ == "__main__":
    grid: list[list[int]] = [
        [1, 1, 1, 1, 1],
        [1, 0, 5, 0, 1],
        [1, 1, 2, 0, 2],
        [1, 0, 0, 0, 1],
        [1, 3, 1, 1, 2],
    ]

    start: tuple[int, int] = (0, 0)
    goal: tuple[int, int] = (4, 4)

    print(
        f"The shortest path cost from {start} to {goal} is: {a_star(grid, start, goal)}"
    )
    print(
        f"The shortest path cost from {(0,0)} to {(4,3)} is: {a_star(grid, (0,0), (4,3))}"
    )
