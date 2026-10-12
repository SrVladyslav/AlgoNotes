"""
This is an interesting problem to solve in an UNDIRECTED tree,
could be also good to select the root node of a graph to transform it into a tree.

Be aware of the case that we can have 1 or 2 center nodes, but there can't to be more than 2 nodes.

Notice that the center is always the middle vertex or middle two vertices of the longest path along the tree.

The approach here is like to peel an onion, iteratively we will be removing
layers of the tree until we reach the center node/nodes.

Steps:
1. Count the degree of each node. Take into account that all the leafs have degree 1.
2. Delete all the nodes with degree 1 and decrese by one the degree of each neighbour node.

Time: O(V + E)
Memory: O(V + E)
"""

from collections import defaultdict, deque


def leaf_peeling(edges: list[tuple[int, int]], nodes_num: int) -> list[int]:
    # 1. Create the graph in dict form , while creating, count the degree of each node
    graph = defaultdict(list[int])  # {node: [neighbours...]}
    degrees = defaultdict(int)  # in-degree and out-degree of each node {node: degree}

    for start, end in edges:
        # Set the graph in both ways since we have an undirected graph
        graph[start].append(end)
        graph[end].append(start)
        # Add the degree of each node
        degrees[start] += 1
        degrees[end] += 1

    # 2. Now, create a queue with the nodes with degree 1, and start processing/ peeling them
    queue = deque([node for node, degree in degrees.items() if degree <= 1])

    # Now what we should do, is run the queue while the processed nodes are not 1 or 2
    remaining_nodes = nodes_num
    while remaining_nodes > 2:
        # Count the quantity of leaves we pruned
        curr_length = len(queue)
        remaining_nodes -= curr_length

        # Prune all the nodes with degree 1 from the queue
        # run all curr_length times since we will be adding new leaves to the queue
        for _ in range(curr_length):
            node = queue.popleft()

            for neighbour in graph[node]:
                # quit one degree for each neighbour
                degrees[neighbour] -= 1

                # If neighbour has more than one degree, add it to the queue
                if degrees[neighbour] == 1:
                    queue.append(neighbour)

    return list(queue)


if __name__ == "__main__":
    # Tree:
    #
    #       0       9
    #       |       |
    #       1 ----- 2 ----- 3
    #               |        / \
    #               6       4   5
    #              / \
    #             7   8

    edges: list[tuple[int, int]] = [
        (0, 1),
        (1, 2),
        (2, 9),
        (2, 3),
        (3, 4),
        (3, 5),
        (2, 6),
        (6, 7),
        (6, 8),
    ]

    print(f"Leafs: {leaf_peeling(edges, 10)}")

    edges_two_centers: list[tuple[int, int]] = [
        (0, 1),
        (2, 1),
        (1, 3),
        (3, 4),
        (3, 5),
    ]  # should be 1 and 3 the centers
    print(f"Leafs 2 centers: {leaf_peeling(edges_two_centers, 6)}")
