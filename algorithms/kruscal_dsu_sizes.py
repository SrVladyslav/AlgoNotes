def kruskal(
    nodes_count: int, edges: list[tuple[int, int, int]]
) -> tuple[int, list[tuple[int, int, int]]]:
    parents: list[int] = list(range(nodes_count))
    size: list[int] = [0] * nodes_count

    def _find(node: int) -> int:
        nonlocal parents
        while node != parents[node]:
            parents[node] = parents[parents[node]]
            node = parents[node]
        return node

    def _union(node_a: int, node_b: int) -> bool:
        nonlocal parents, size
        root_a = _find(node_a)
        root_b = _find(node_b)

        if root_a == root_b:
            return False

        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parents[root_b] = root_a
        size[root_a] += size[root_b]

        return True

    # Kruscal
    edges.sort(key=lambda x: x[2])  # Sort by the length
    result: list[tuple[int, int, int]] = []
    min_cost: int = 0  # Min cost of the MST

    for start, end, weight in edges:
        if not _union(start, end):
            continue  # Is cycle, so just skip it

        min_cost += weight
        result.append((start, end, weight))

        # Early start: Graph -> E = V - 1  -> V <- E -> V
        if len(result) > nodes_count:
            break

    # Graph is disconnected
    if len(result) != nodes_count - 1:
        return -1, []

    return min_cost, result


if __name__ == "__main__":
    edges: list[tuple[int, int, int]] = [
        (0, 1, 1),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 3),
    ]

    cost, mst = kruskal(4, edges)

    print("Cost:", cost)
    print("MST:", mst)
