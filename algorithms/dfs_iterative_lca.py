class Node:
    def __init__(self, value: int, children: list["Node"]):
        self.value = value
        self.children = children


def find_lca_tree(root: Node, *values: int) -> int:
    if not root:
        return -1

    # node -> how many targets were found in its subtree
    found_count: dict[Node, int] = {}

    stack = [(root, False)]  # False is indication flag for preprocessed

    while stack:
        node, visited = stack.pop()

        if not visited:
            # Enter phase : mark as visited, so the next time will do post recursion stuff
            stack.append((node, True))

            for child in reversed(node.children):
                stack.append((child, False))

        else:
            # EXIT / POSTORDER phase
            found = int(node.value in values)

            for child in node.children:
                found += found_count[child]  # Add the found count of the children

            if found >= len(values):
                return node.value

            found_count[node] = found  # Update the found count of the current node

    return -1  # Nothing found


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
    print(f"Find the LCA of 14, 16 and 10: {find_lca_tree(root, 14, 16, 10)}")  # 0
