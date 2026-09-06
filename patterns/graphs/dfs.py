"""
Solve the maze problem using DFS.
O is avaiblable and 1 is blocked.


start = [0, 0]
end = [10, 14]

graph = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
]

result = True

Time: O(n+m)
Memory: O(n)
"""

from pprint import pprint


def in_bounds(x: int, y: int, graph: list[list[int]]) -> bool:
    return 0 <= x < len(graph) and 0 <= y < len(graph[0])


def dfs(graph: list[list[int]], start: list[int], end: list[int]) -> bool:
    """
    Deep first search algorithm, the difference fro mthe BDF is that we are using LIFO here instead of FIFO.
    """
    # =============================================================================
    # Step 1: Basically we define the stack and the visited points
    # =============================================================================
    stack: list[tuple[int, int]] = [(start[0], start[1])]
    visited: set[tuple[int, int]] = {(start[0], start[1])}

    # Directions allowed to move inside the graph
    directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while stack:
        # =============================================================================
        # Step 2: Get the top element from the stack in order to check if is is the end or we should continue searching
        # =============================================================================
        x, y = stack.pop()  # Last element -> LIFO

        # Ending condition
        if x == end[0] and y == end[1]:
            return True

        # =============================================================================
        # Step 3: Check all the neighbours to the current node: only if they are in bounds and not visited
        # If is not in the end, we should add all the neighbours to the stack and continue searching
        # Here all the next nodes are inside the grid, so we will try to go through all the directions
        # =============================================================================
        for move_x, move_y in directions:
            new_x = x + move_x
            new_y = y + move_y

            # =============================================================================
            # Step 4: Now we should check if the new values are in bounds, and if the new values are not visited or allowed
            # =============================================================================
            if (
                in_bounds(new_x, new_y, graph)
                and (new_x, new_y) not in visited
                and graph[new_x][new_y] == 0
            ):
                stack.append((new_x, new_y))
                visited.add((new_x, new_y))

    return False


if __name__ == "__main__":
    start: list[int] = [0, 0]
    end: list[int] = [10, 14]

    graph: list[list[int]] = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    print(f"Is the path from {start} to {end} in the following graph?")
    pprint(graph)
    print(f"Result: {dfs(graph, start, end)}")
