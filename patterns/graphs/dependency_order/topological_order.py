"""
Given a graph representing some tasks, where each task has some dependencies before it.
You should find the order in which the tasks should be executed to make
sure that all the dependencies are met. If there are many responses, we can return
the one we want. If there is a cycle, we should return an empty list.

e.g.

graph= [[2,1],[9,1],[9,8],[1,7], [1,8], [7],[8],[11,4],[4,8]]

response = [2,9,11,1,4,7,8 ]

That problem is a topology problem, so we can solve it by using the Kahn algorithm.
Like a perceptron, we count first the number of nodes entering each node, aka in-degree.


 * We should check for the Kahn algoritm:
 * 1) Count how many inputs each node has (in-degree).
 * 2) Where there is a cycle, we should return an empty list.
 * 3) If the input has no incoming edges, then we add them into a queue, as in BFS. They
 *    should always have in-degree = 0
 * 4) While queue exists, we get the front value and remove it from the queue and add to result
 * 5) Go to all the neighbors of the current node and decrease their in-degree by 1.
 * 6) During the loop, if the in-degree = 0, then we add it to the queue.


"""

from collections import deque
from patterns.graphs.lib import graph_from_edges


def build_indegree(graph: dict[str, list[str]]) -> dict[str, int]:
    indegree: dict[str, int] = (
        {}
    )  # Basically this is the counter of how many nodes are entering this node

    for node in graph:
        # Add the current node to the indegree list, from start is 0 since we don't actually know
        # how many nodes are entering this node.
        indegree.setdefault(node, 0)
        # Check the neighbours now
        for neighbour in graph[node]:
            indegree[neighbour] = indegree.get(neighbour, 0) + 1
    return indegree


def kahn_topological_order(graph: dict[str, list[str]]) -> list[int]:
    # Stage 1: Initialization of all the parts
    indegree: dict[str, int] = build_indegree(graph)
    queue = deque([node for node in indegree if indegree[node] == 0])
    order: str = []

    # Stage 2: Process the BFS queue of neighbours
    while queue:
        node: str = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            # Stage 3: Decrease the neighbour indegree by one and add to queue if is 0
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # Stage 4: Check for loops
    if len(order) != len(indegree):
        return [-1]

    return order


if __name__ == "__main__":
    graph: dict[str, list[str]] = {
        "1": ["7", "8"],
        "2": ["1"],
        "4": ["8"],
        "7": [],
        "8": [],
        "9": ["1", "8"],
        "11": ["4"],
    }

    print(f"Graph: {graph}")
    print(f"Order: {kahn_topological_order(graph)}")
