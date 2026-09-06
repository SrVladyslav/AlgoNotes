"""
Time: O(n*m)
Memory: O(n*m)
"""

from collections import deque


def in_bounds(x: int, y: int, graph: list[list[int]]) -> bool:
    return 0 <= x < len(graph) and 0 <= y < len(graph[0])


def find_start(graph: list[list[int]]) -> list[int]:
    """
    If we need to start randomly in the graph
    """
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == 2:
                return [row, col]
    return [-1, -1]


def shortest_path(graph: list[list[int]]) -> int:
    # =============================================================================
    # Stage 1: Where is BFS starting=?
    # MAIN PROBLEM IS TO FIGURE OUT THAT WE NEED TO USE THE BFS
    # =============================================================================
    start = ...

    queue: deque = deque(
        [(start[0], start[1], 0)]
    )  # Counters are added too if needed :)
    visited: set[tuple[int, int]] = {
        (start[0], start[1])
    }  # Remember your last girlfriend and don't walk nearby :)

    directions: list[tuple[int, int]] = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]  # This is just for this types of graphs

    while queue:
        row, col, dist = queue.popleft()

        # =============================================================================
        # Stage 2: Processing the current path, node and result basically
        # =============================================================================
        ...

        # =============================================================================
        # Stage 3: Loop over your neightbours
        # =============================================================================
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            # =============================================================================
            # Stage 4: Decide which neighbours to add to the queue
            # =============================================================================
            if ...:
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))

    return -1  # If there are no path
