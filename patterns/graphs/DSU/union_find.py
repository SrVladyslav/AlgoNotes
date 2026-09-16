"""
DSU or commonly known as Union-Find, is an algorithm that allows us to find the connected
components of a graph. It is an auxiliary data structure that can be used to solve problems related to
graphs, such as finding if two vetices are connected, is the graph has a cycle. etc.

Basically is a data structure that shows you which nodes are from the same component.

"""


class UnionFind:
    """
    The base idea is to create an array for parent and rank which shows how many nodes the
    parent has. Here is the path compressed implementation.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))  # Representsbasically all the nodes of the graph
        self.size = [1] * n  # Represents the number of nodes in the component

    def _find(self, x: int) -> int:
        """
        Run over the parent array while the node is not the same as the current node (parent of parent, final one)
        """
        while self.parent[x] != x:
            # Path compression
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def _union(self, a: int, b: int) -> bool:
        root_a = self._find(a)
        root_b = self._find(b)

        # If the roots are the same, then they are already connected,
        # meaning that if we connects them, we will create a cycle
        if root_a == root_b:
            return False

        # Now we need to update the ranks of the nodes and merge them,
        # The smaller goes before the larger. Here root_a should be bigger
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        # Now since rank_a is bigger, we add it as parent to rank b
        self.parent[root_b] = root_a
        # Finally we update the rank by adding the b nodes counter to a
        self.size[root_a] += self.size[root_b]

        return True

    def count_connected_components(self) -> int:
        """
        Since we have the Path Compression, all the nodes in parent are pointing to parents,
        meaning that the n of components is the number of different parents.
        """
        s = set(self.parent)
        return len(s)

    def has_cycle(self, edges: list[list[int, int]]) -> bool:
        for u, v in edges:
            if not self._union(u, v):
                return True
        return False

    def edges_to_be_removed_to_break_cycle(
        self, n: int, edges: list[list[int, int]]
    ) -> list[list[int, int]]:
        to_remove: list[list[int, int]] = []
        uf = UnionFind(n)
        for from_node, to_node in edges:
            if not uf._union(from_node, to_node):
                to_remove.append([from_node, to_node])

        return to_remove


if __name__ == "__main__":
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    # edges = [[1, 2], [2, 3], [3, 4], [1, 5]]

    uf = UnionFind(6)
    print(f"Graph: {edges}")
    print(f"Has cycle: {uf.has_cycle(edges)}")
    print(f"Number of connected components: {uf.count_connected_components()}")
    print(
        f"Edges to be removed to break the cycle: {uf.edges_to_be_removed_to_break_cycle(6,edges)}"
    )
    print(f"Parent: {uf.parent}")
