"""
* This is a Graph problem where we should search for the topologycal order.
*
* Time: O(n+m)
* Memory: O(n)
"""

from collections import deque


def kahn_topological_sort(graph: dict[str, list[int]]) -> list[int]:
    # =============================================================================
    # 1) Initialization
    # =============================================================================
    indegree = ...
    queue: deque = deque([node for node in indegree if indegree[node] == 0])
    order = []

    # =============================================================================
    # 2) Process the queue, BFS by in-degree. Process the neighbours, decrease
    # the indegree and add to the queue if it is 0.
    # =============================================================================
    while queue:
        # =============================================================================
        # 3) Preprocess the head from the queue start
        # =============================================================================
        node = queue.popleft()
        order.append(node)

        # =============================================================================
        # 4) Process the neighbours of the current node
        # MAIN PROBLEM IS TO CORRECTLY LOOP OVER THE NEIGHBOURS AND CHECK FOR CYCLES
        # =============================================================================
        for neighbour in graph[node]:
            ...

    # =============================================================================
    # 5) Check for the loop
    # =============================================================================
    if len(order) != len(indegree):
        return []

    return order
