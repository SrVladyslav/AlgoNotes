"""
We have a graph, and we have the initial node and various end nodes.
We need to find the shortest path between the initial node and some of the end nodes and return the value.

e.g.
[
[0,0,0,1,0,0],
[0,1,0,1,0,1]
[0,1,1,0,0,1]
[0,0,0,0,1,1]
]

start = [3, 0]
end= [[0,5],[1,2]]

response= 5 (The shortest path)
"""


def shortest_path(
    graph: list[list[int]], start: list[int], end: list[list[int]]
) -> int:
    # We will be using BFS here, so counter will be added to know how much we are going from the start
    queue: list[tuple[int, int]] = [(start[0], start[1], 0)]
    # Visited nodes are the same approach, just the ones which should bnot be repeated
    visited: set[tuple[int, int]] = {(start[0], start[1])}

    # Since we have a board and we need to check the neighbours in 4 directions, we will use a list of directions
    directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Now we will iterate to search over the graph
    while queue:
        # get the first element from the list and process it
        x, y, distance = queue.pop(0)

        # Now we check for the base case, to see if we are in the end or not yet
        if [x, y] in end:
            return distance

        # Now we will try to generate all the neightburs to the current node
        for move_x, move_y in directions:
            new_x = x + move_x
            new_y = y + move_y

            # Before nothing, we should check if we still in bounds, if the node was not visited and the most important,
            # if the node is not a wall of course
            if (
                0 <= new_x < len(graph)
                and 0 <= new_y < len(graph[0])  # Is in bound of the grid (graph)
                and (new_x, new_y) not in visited  # Is allowed to search over there
                and graph[new_x][new_y] == 0  # In not a wall
            ):
                # Once we know that is allowed to search, we shoudl generate all those nodes, add distance and save
                # them to the queue to be processed later
                queue.append((new_x, new_y, distance + 1))
                visited.add((new_x, new_y))

    return -1  # If there are no path


if __name__ == "__main__":
    graph: list[list[int]] = [
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1],
    ]
    start: list[int] = [3, 0]
    end: list[list[int]] = [[0, 5], [1, 2]]

    print(f"Shortest path from {start} to {end}: {shortest_path(graph, start, end)}")
