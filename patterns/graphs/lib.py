from collections import defaultdict


# Not oriented_graph
def graph_from_edges(
    edges: list[list[int]], is_directed: bool = False
) -> dict[int, list[int]]:
    grapth = defaultdict(list)
    for u, v in edges:
        grapth[u].append(v)
        if not is_directed:
            grapth[v].append(u)

    return grapth
