"""
Given a graph unordered, we wanna know the number
of connections between two nodes.

e.g.

graph: dict[int, list[int]] = {
    1: {2},
    2: {1, 3},
    3: {2, 4, 5},
    4: {3, 7},
    5: {3, 7},
    7: {4, 5},
}

ini=5
end=1

result = 3


Time: O(n+m)
Memory: O(n)
"""


def shortest_path(graph: dict[int, list[int]], start: int = 0, finish: int = 0) -> int:
    # =============================================================================
    # Stage 1: Initialize the queue or deque. Queue inside has the deque
    # =============================================================================
    queue: list[tuple[int, int]] = [(start, 0)]
    visited: set[int] = {start}

    while queue:
        # =============================================================================
        # Stage 2: Loop while we have elements in the queue.
        # Get the first element of the queue and process it looking for the solution
        # =============================================================================
        node, distance = queue.pop(0)

        # We check if the node is the finish or not, so we know if to continue or not
        if node == finish:
            return distance

        # Explore now for all the nodes that are connected to this one
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                # Add the current node to visited, so we don't visit it again
                visited.add(node)

    return -1


if __name__ == "__main__":
    graph: dict[int, list[int]] = {
        1: {2},
        2: {1, 3},
        3: {2, 4, 5},
        4: {3, 7},
        5: {3, 7},
        7: {4, 5},
    }

    ini: int = 5
    end: int = 1

    print(
        f"Number of connections from {ini} to {end}: {shortest_path(graph= graph, start=ini, finish=end)}"
    )
