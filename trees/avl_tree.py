class Node:
    def __init__(self, value: int):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None  # Crucial fo rmainataining the tree balanced.


class AVLTree:
    """


    Cases with condition
        Left-Left (LL) -> Node: BF > +1, Left child: BF >= 0
        Right-Right (RR -> Node: BF < -1, Right child: BF <= 0
        Left-Right (LR) -> Node: BF > +1, Left child: BF < 0
        Right-Left (RL) -> Node: BF < -1, Right child: BF > 0
    """

    def __init__(self):
        self.root = None

    def _right_rotate(self, node: Node) -> Node:
        # Node unbalanced on the lift side
        # Rotate the nodes the same way as it does in the red black tree
        temp = node.left
        T3 = temp.right

        temp.right = node
        node.left = T3

        # Update the heights. This ensures that the branches are balanced
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        temp.height = 1 + max(self.height(temp.left), self.height(temp.right))

        return temp

    def _left_rotate(self, node: Node) -> Node:
        # node is unbalanced on the right side
        # Rotate the nodes the same was as it does in the red black tree implementation
        temp = node.right
        T2 = temp.left

        temp.left = node
        node.right = T2

        # Update the heights. This ensures that the branches are balanced
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        temp.height = 1 + max(self.height(temp.left), self.height(temp.right))

        return temp

    def _left_right_rotate(self, node: Node) -> Node:
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _right_left_rotate(self, node: Node) -> Node:
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    def _rebalance(self, node: Node) -> Node:
        balance_factor = self.get_balance_factor(node)

        if balance_factor > 1:
            if self.get_balance_factor(node.left) < 0:
                return self._left_right_rotate(node)
            return self._right_rotate(node)

        if balance_factor < -1:
            if self.get_balance_factor(node.right) > 0:
                return self._right_left_rotate(node)
            return self._left_rotate(node)

        return node

    def height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node: Node) -> int:
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def _rebalance_path(self, path: list) -> None:
        # Walks the recorded descent path bottom-up, fixing height and balance
        # at every ancestor of a subtree that just changed. Since Node has no
        # parent pointer, `path` (root-first) is how we find our way back up
        # and re-link a rotated subtree into its parent.
        for i in range(len(path) - 1, -1, -1):
            node = path[i]
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            new_subtree_root = self._rebalance(node)

            if i == 0:
                self.root = new_subtree_root
            elif new_subtree_root is not node:
                parent = path[i - 1]
                if parent.left is node:
                    parent.left = new_subtree_root
                else:
                    parent.right = new_subtree_root

    def insert(self, value: int) -> None:
        # Insertion logic of the regular binary search tree, done iteratively
        if self.root is None:
            self.root = Node(value)
            return

        path = []
        current = self.root
        while True:
            path.append(current)
            if current.value == value:
                return  # Value already present, nothing to insert/rebalance
            if value <= current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right

        # Walk back up from the new leaf's parent, fixing heights/balance
        self._rebalance_path(path)

    def delete(self, value: int) -> None:
        # Deletion logic of the regular binary search tree, done iteratively
        if self.root is None:
            return

        path = []  # Ancestors of the node being removed, root-first
        current = self.root
        while current is not None and current.value != value:
            path.append(current)
            current = current.left if value < current.value else current.right

        if current is None:
            return  # Value not found, nothing to delete

        node = current
        if node.left is not None and node.right is not None:
            # Two children: replace the value with the inorder successor
            # (the minimum of the right subtree), then remove that successor
            # node instead, which has at most a right child.
            path.append(node)
            successor = node.right
            while successor.left is not None:
                path.append(successor)
                successor = successor.left
            node.value = successor.value
            node = successor

        # `node` now has at most one child, so it can simply be spliced out
        child = node.left if node.left is not None else node.right
        if path:
            parent = path[-1]
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child

        # Walk back up from the splice point, fixing heights/balance
        self._rebalance_path(path)


def _inorder(node: Node) -> list:
    if node is None:
        return []
    return _inorder(node.left) + [node.value] + _inorder(node.right)


def _is_balanced(tree: AVLTree, node: Node) -> bool:
    if node is None:
        return True
    if abs(tree.get_balance_factor(node)) > 1:
        return False
    return _is_balanced(tree, node.left) and _is_balanced(tree, node.right)


if __name__ == "__main__":
    tree = AVLTree()

    for value in [10, 5, 2, 4, 3, 15, 20, 1, 6, 8, 7]:
        tree.insert(value)

    print(f"Inorder after inserts: {_inorder(tree.root)}")
    print(f"Balanced after inserts: {_is_balanced(tree, tree.root)}")

    tree.delete(10)  # two-children case (root)
    print(f"Inorder after deleting 10: {_inorder(tree.root)}")
    print(f"Balanced: {_is_balanced(tree, tree.root)}")

    tree.delete(1)  # leaf case
    print(f"Inorder after deleting 1: {_inorder(tree.root)}")
    print(f"Balanced: {_is_balanced(tree, tree.root)}")

    tree.delete(15)  # one-child case
    print(f"Inorder after deleting 15: {_inorder(tree.root)}")
    print(f"Balanced: {_is_balanced(tree, tree.root)}")

    tree.delete(999)  # value not present, should be a no-op
    print(f"Inorder after deleting missing value: {_inorder(tree.root)}")

    for value in [20, 4, 3, 2, 6, 7, 8]:
        tree.delete(value)
    print(f"Inorder after emptying most of the tree: {_inorder(tree.root)}")
    print(f"Root: {tree.root.value if tree.root else None}")
