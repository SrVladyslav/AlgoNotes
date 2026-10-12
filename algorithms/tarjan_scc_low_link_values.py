def tarjan_scc_low_link_values(
    vertices: int, edges: list[tuple[int, int]]
) -> list[list[int]]:
    """
    Finds all Strongly Connected Components (SCC) in a directed graph using Tarjan's algorithm.

    A SCC is a group of vertices where every vertex can reach every other vertex in the same component.

    Core idea:
    Tarjan performs a DFS and assigns each vertex two values:

        discovery[node] -> The DFGS order in which the node was first visited.

        low[node] -> The smallest discovery index reachable from this node whil e
                    staying inside the current DFS exploration.

    The low-link values tells us whether a node can reach an ancestor in the current DFS path.

    Steps:
    1. Run DFS from every unvisited vertex (Like when counting different components with BFS).
    2. When visiting a node:
        - Assign its discovery index.
        - Set low[node] = discovery [node]
        - Push the node into the stack
        - Mark it as currently active in the DFS stack.
    3. For every neighbour:

        Case A: The neighbour has not been visited.
            Recursively visit it, then propagate its los-lonk value:

                low[node] = min(low[node], low[neighbour])

            If the child can reach an older ancestor, then the current node can also reach that ancestor.

        Case B: The neighbour is already in the current DFS stack.
            This means we found an edge back into the current active DFS region.

                low[node] = min(low[node], discovery[neighbour])

            We use discovery[neighbour], not low[neghbour], because we only want to connect the current node
            to an ancestor that is still part of the active DFS component.
    4. After exploring all neighbors, check:

        low[node] == discovery[node]

        If is True, this node is the root of a Strongly Connected Component.
        Why?
        Because none of he nodes below it can reach any vertex that was discovered before this node while remaining
        inside the current active DFS stack.

    5. Pop nodes from the stack until the current node is removed. All popped nodes
        belong to the same SCC.

    Why the stack is necessary?
        A visited node is not alwats part of the current SCC candidate.
        Once an SCC is completed and removed from the stack , later edges
        pointing to that SCC must not affect low-link values.


    Example:

        0 -> 1 -> 2
        ^         |
        |_________|

        2 -> 3 -> 4
             ^    |
             |____|

    SCCs:
        [0, 1, 2]
        [3, 4]

    Time Complexity:
        O(V + E)

    Space Complexity:
        O(V + E)

    Where:
        V = number of vertices
        E = number of edges
    """

    # Construct a dict based graph
    graph: list[list[int]] = [[] for _ in range(vertices)]

    for start, end in edges:
        graph[start].append(end)

    # Tarjan's algorithm
    discovery: list[int] = [-1] * vertices
    low: list[int] = [-1] * vertices

    stack: list[int] = []
    in_stack: list[bool] = [False] * vertices

    components: list[list[int]] = []
    time = 0

    def _dfs(node: int) -> None:
        nonlocal time

        discovery[node] = time
        low[node] = time
        time += 1

        stack.append(node)
        in_stack[node] = True

        for neighbour in graph[node]:
            # tree edge: neighbour has not been visited yet.
            if discovery[neighbour] == -1:
                _dfs(neighbour)

                low[node] = min(low[node], low[neighbour])

            # back edge to a node that is still part of the current active DFS region.
            elif in_stack[neighbour]:
                low[node] = min(low[node], discovery[neighbour])

        # If node cannot reach any earlier active vertex,
        # the it is the root of an SCC:
        if low[node] == discovery[node]:
            component: list[int] = []

            while True:
                current = stack.pop()
                in_stack[current] = False
                component.append(current)

                if current == node:
                    break

            components.append(component)

    # explore all the remaining nodes
    for node in range(vertices):
        if discovery[node] == -1:
            _dfs(node)

    return components


if __name__ == "__main__":

    vertices = 8

    edges = [
        # 1
        (0, 1),
        (1, 2),
        (2, 0),
        # 2
        (2, 3),
        # 3
        (3, 4),
        (4, 5),
        (5, 3),
        # 4
        (5, 6),
        # 5
        (6, 7),
        (7, 6),
    ]

    print(tarjan_scc_low_link_values(vertices, edges))
