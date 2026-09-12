from heapq import heappush, heappop


def dijkstra(
    graph: dict[str, list[tuple[str, int]]],
    start: str,
) -> tuple[dict[str, int], dict[str, str]]:
    """
    Shortest path from one source to all other nodes.
    """
    if graph == None:
        return {}, {}

    # Initialization of th ethings
    distances: dict[str, int] = {node: float("inf") for node in graph}
    distances[start] = 0
    previous: dict[str, tuple[str, int]] = {start: None}
    min_heap: list[tuple[str, int]] = [(start, 0)]

    while min_heap:
        # Extract the minimum element from the heap
        node, distance = heappop(min_heap)

        # Pass if the current distance is larger
        if distances[node] > distance:
            continue

        # update the neighbours
        for neighbour, weight in graph[node]:
            new_distance: int = distance + weight

            if distances[neighbour] > new_distance:
                distances[neighbour] = new_distance
                heappush(min_heap, (neighbour, new_distance))
                previous[neighbour] = node

    return distances, previous


def find_path(
    graph: dict[str, list[tuple[str, int]]], start: str, end: str
) -> tuple[list[str], int]:
    if graph == None or end not in graph or start not in graph:
        return []

    # get the distances and the previous dist
    distances, previous = dijkstra(graph, start)

    path: list[str] = []

    node: str = end
    while node != start:
        path.append(node)
        node = previous[node]
    path.append(start)

    return path, distances[end]


if __name__ == "__main__":
    # The graph
    graph: dict[str, list[tuple[str, int]]] = {
        "A": [("B", 2), ("D", 8)],
        "B": [("A", 2), ("D", 5), ("E", 6)],
        "C": [("E", 9), ("F", 3)],
        "D": [("A", 8), ("B", 5), ("E", 3), ("F", 2)],
        "E": [("B", 6), ("C", 9), ("D", 3), ("F", 1)],
        "F": [("C", 3), ("D", 2), ("E", 1)],
    }

    # Find the shortest path value fropm A to C
    print(f"Distances with dijkstra: {dijkstra(graph, "A")}")

    print(f"Path from A to C: {find_path(graph, 'A', 'C')}")
