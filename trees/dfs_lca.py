from collections import deque, defaultdict

""" 
This approach is optimal for one query and not for multiple queries, since it searches from start every time. 

Time: O(n) 
Memory: O(h) where h is the height of the tree
"""


class Node:
    def __init__(self, value: int, children: list["Node"]):
        self.value = value
        self.children = children


def find_lca_tree(root: Node, val_1: int, val_2: int) -> int:
    if not root:
        return None

    def _search(node: Node) -> tuple[int | None, int | None]:  # (found value, lca)
        # Base case, found a node
        results: list[tuple[int | None, int | None]] = []

        # Base case for checking if we have found the base value in this node
        if node.value in (val_1, val_2):
            print("Found", node.value)
            results.append((node.value, None))

        # The base case is implicit inside the node.children
        for child in node.children:
            child_found, lca = _search(child)
            if lca is not None:
                return child_found, lca  # Propagate the solution to the root

            elif child_found is not None:
                results.append(
                    (child_found, lca)
                )  # Append the current found node to process it later

        # If we have two results, then we found the LCA, which is the current node
        if len(results) == 2:
            return results[0][0], node.value

        elif results:
            return results[0]

        return None, None

    res = _search(root)
    return res[1] if res else root.value


if __name__ == "__main__":
    # Tree:
    #
    #                         0
    #                       /   \
    #                      1     2
    #                    /  \   / | \
    #                   3    4 5  6  7
    #                  / \    / \    / \
    #                 8   9 10 11  12  13
    #                         / | \
    #                       14 15 16
    root = Node(
        0,
        [
            Node(1, [Node(3, [Node(8, []), Node(9, [])]), Node(4, [])]),
            Node(
                2,
                [
                    Node(
                        5,
                        [
                            Node(10, []),
                            Node(11, [Node(14, []), Node(15, []), Node(16, [])]),
                        ],
                    ),
                    Node(6, []),
                    Node(7, [Node(12, []), Node(13, [])]),
                ],
            ),
        ],
    )

    print(f"Find the LCA of 13 and 14: {find_lca_tree(root, 13, 14)}")  # 2
    print(f"Find the LCA of 10 and 5: {find_lca_tree(root, 10, 5)}")  # 5
    print(f"Find the LCA of 13 and 3: {find_lca_tree(root, 13, 3)}")  # 0
