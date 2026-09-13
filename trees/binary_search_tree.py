from collections import deque


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, value: int) -> None:
        new_node: TreeNode = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current: TreeNode = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

            else:
                return  # Value already present in the tree, ignore it

    def search(self, value: int) -> TreeNode | None:
        current: TreeNode = self.root

        while current:
            if value == current.value:
                return current

            current = current.left if value < current.value else current.right

        return None

    def is_balanced(self) -> bool:
        current: TreeNode | None = self.root
        if current is None:
            return True

        stack: deque[tuple[TreeNode, bool]] = deque([(current, False)])
        heights: dict[TreeNode, int] = {}

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if not visited:
                # Postorder: process children before parent
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))

            else:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                if abs(left_height - right_height) > 1:
                    return False

                heights[node] = 1 + max(left_height, right_height)

        return True

    def print_tree(self) -> None:
        current: TreeNode | None = self.root
        if current is None:
            print("Empty tree")
            return

        queue = deque([current])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()

                level.append(node.value)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            print(level)


if __name__ == "__main__":

    # --------------------------------
    # Example 1: Balanced BST
    #
    #         10
    #        /  \
    #       5    15
    #      / \
    #     3   7
    #
    # --------------------------------

    tree1 = BinarySearchTree()

    for value in [10, 5, 15, 3, 7]:
        tree1.insert(value)

    print("Tree 1:")
    tree1.print_tree()

    print("Balanced:", tree1.is_balanced())
    print()

    # --------------------------------
    # Example 2: Not balanced
    #
    #     1
    #      \
    #       2
    #        \
    #         3
    #          \
    #           4
    #
    # --------------------------------

    tree2 = BinarySearchTree()

    for value in [1, 2, 3, 4]:
        tree2.insert(value)

    print("Tree 2:")
    tree2.print_tree()

    print("Balanced:", tree2.is_balanced())
    print()

    # --------------------------------
    # Example 3: Perfect BST
    #
    #         8
    #       /   \
    #      4     12
    #     / \    / \
    #    2   6  10  14
    #
    # --------------------------------

    tree3 = BinarySearchTree()

    for value in [8, 4, 12, 2, 6, 10, 14]:
        tree3.insert(value)

    print("Tree 3:")
    tree3.print_tree()

    print("Balanced:", tree3.is_balanced())
