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


"""


def dependency_order(graph: list[list[int]]) -> list[int]: ...


if __name__ == "__main__":
    graph: list[list[int]] = [
        [2, 1],
        [9, 1],
        [9, 8],
        [1, 7],
        [1, 8],
        [7],
        [8],
        [11, 4],
        [4, 8],
    ]
    print(f"Graph: {graph}")
    print(f"Order: {dependency_order(graph)}")
