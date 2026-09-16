class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        # Already connected -> adding this edge would create a cycle
        if root_a == root_b:
            return False

        # Union by rank
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a

        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

        return True


def kruskal(
    vertices: int, edges: list[tuple[int, int, int]]
) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Finds the Minimum Spanning Tree (MST).

    Edges:
        (from_vertex, to_vertex, weight)

    Returns:
        (total_weight, mst_edges)

    Time: O(E*log(E))
    Memory: O(V)

    1. Sort edges by weight
    2. Take the cheapest edge
    3. Add it if it doesn't create a cycle
    4. Stop after V - 1 edges
    """

    # Sort the edges by weight
    edges.sort(key=lambda edge: edge[2])

    uf = UnionFind(vertices)

    total_cost: int = 0
    mst_edges = []
    for from_vertex, to_vertex, weight in edges:
        # Add edge only if it does not create a cycle
        if uf.union(from_vertex, to_vertex):
            mst_edges.append((from_vertex, to_vertex, weight))
            total_cost += weight

            # MST always contains V - 1 edges
            if len(mst_edges) == vertices - 1:
                break

    # Graph is disconnected
    if len(mst_edges) != vertices - 1:
        return -1, []

    return total_cost, mst_edges


if __name__ == "__main__":
    edges = [
        (0, 1, 1),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 5),
        (2, 3, 3),
    ]

    cost, mst = kruskal(4, edges)

    print("Cost:", cost)
    print("MST:", mst)
