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

    def insert(self, value: int) -> None:
        # Insertion loginh of the regular binary search tree
        current = self.root
        while current != None:
            if current.value == value:
                break
            if value <= current.value:
                if current.left == None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = Node(value)
                    break
                current = current.right

        # Update the heights of the root node
        self.root.height = 1 + max(
            self.height(self.root.left), self.height(self.root.right)
        )
        # Perform the rebalance operation on the root, since it checks if the
        # balance was broken and it should rebalance something
        return self.rebalance(self.root)

    def delete(self, value: int) -> None:
        # Deletion login of a binary tree here
        ...
        # Update the heights of the root node
        self.root.height = 1 + max(
            self.height(self.root.left), self.height(self.root.right)
        )
        # Perform the rebalance operation on the root, since it checks if the
        # balance was broken and it should rebalance something
        return self.rebalance(self.root)


if __name__ == "__main__":
    tree = AVLTree()

    tree.insert(10)
    tree.insert(5)
    tree.insert(2)
    tree.insert(4)
    tree.insert(3)
    tree.delete(10)
