"""
Red black tree si a self balanced binary search tree,
where leaf nodes are considered black by default.

Properties:
1: Every node is either RED or BLACK.
2: The root is ALWAYS BLACK.
3: Every leaf (NIL) is BLACK.
4: If a node is RED, both children are BLACK.
5: Every path from a node to its descendant NIL nodes
must have the same number of black nodes.

h <= 2h(b)

n >= 2**(h(b))-1
Solving the equation:

h <= 2 log(n+1)
"""


class Node:
    def __init__(self, data: int, color: str = "red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(
            data=None, color="black"
        )  # Sentinel node, represents the leaf nodes
        self.root = self.NIL
        self.NIL.left = self.NIL.right = self.NIL

    def _rotate_left(self, node: Node) -> None:
        right_child: Node = node.right  # Get the future parent
        # Get the right children to have a new parent which should be inserted
        node.right = right_child.left

        if right_child != self.NIL:
            right_child.left.parent = node

        right_child.parent = (
            node.parent
        )  # update the parent of the right children, since it would be in the place of node now
        # If the node parent if NULL, it means it is the root, so the right child should occupy
        # Its place now
        if node.parent is None:
            self.root = right_child

        # If the node has parent and it's on the left side, then the new child should go also there
        elif node == node.parent.left:
            node.parent.left = right_child
        # Finally if the node was going to the right of the parent, then place there the new child too
        else:
            node.parent.right = right_child

        # Now, we should put the remaining re-location there, since we turning left,
        # the new node should go on the left children
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node: Node) -> None:
        # Save the left child, since it will be the ne parent
        left_child: Node = node.left
        # Now we want the current parent node to point to the right node of the left child
        node.left = left_child.right

        # If the right children is not none, then it should point to a new parent, which is the moved node.
        if left_child.right != self.NIL:
            left_child.right.parent = node

        # Now the new left child is has the parent of the old node, since it will be in his place
        left_child.parent = node.parent
        # Now we need to update the parents of the left child to theold node's one
        if node.parent is None:
            self.root = left_child  # It starts to be the root itself

        elif node.parent.right == node:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def _fix_insert(self, node: Node) -> None:
        # Coding conditions for the red black tree rules. Is a bible, ask ChatGPT
        while (
            node.parent and node.parent.color == "red"
        ):  # While is violating the RBT properties
            if (
                node.parent == node.parent.parent.left
            ):  # Parent of the node is the left child of the grandparent
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent

                else:
                    if node == node.parent.right:  # Uncle is black
                        node = node.parent
                        self._rotate_left(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(
                        node.parent.parent
                    )  # R Rotation on the grandparent to correct the violation

            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent

                else:
                    if node == node.parent.left:  # Uncle is black
                        node = node.parent
                        self._rotate_right(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)

        self.root.color = "black"  # Ensure that the root is always black

    def _fix_delete(self, node: Node) -> None:
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self._rotate_left(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self._rotate_right(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self._rotate_left(node.parent)
                    node = self.root

            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self._rotate_right(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == "black" and sibling.left.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self._rotate_left(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self._rotate_right(node.parent)
                    node = self.root
        node.color = "black"

    def _transplant(self, u, v):
        # Used during deletion to replace one subtree with another
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def search(self, node, key: int) -> Node | None:
        if node == self.NIL or key == node.data:
            return node

        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def minimum(self, node: Node) -> Node | None:
        # Finds the node with the minimum value in the tree
        while node.left != self.NIL:
            node = node.left
        return node

    def insert(self, data: int) -> None:
        new_node: Node = Node(data=data)
        new_node.left = new_node.right = self.NIL

        parent = None
        current = self.root

        # Find the correct position for the new node in the tree
        while current != self.NIL:
            parent = current
            # Bionary tree insert logic :,)
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:  # Tree initially empty
            self.root = new_node

        elif new_node.data < parent.data:
            parent.left = new_node

        else:
            parent.right = new_node

        # OH May gad: Fix any color violations in the tree props
        self._fix_insert(new_node)

    def delete(self, data: int) -> None:
        node = self.search(self.root, data)

        if node == self.NIL:
            print(f"Value {data} not found in the tree.")
            return

        temp = node
        temp_original_color = temp.color

        if node.left == self.NIL:
            child = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            child = node.left
            self._transplant(node, node.left)
        else:
            temp = self.minimum(node.right)
            temp_original_color = temp.color
            child = temp.right
            if temp.parent == node:
                child.parent = temp
            else:
                self._transplant(temp, temp.right)
                temp.right = node.right
            self._transplant(node, temp)
            temp.left = node.left
            temp.left.parent = temp
            temp.color = node.color

        if temp_original_color == "black":
            self._fix_delete(child)


if __name__ == "__main__":
    tree = RedBlackTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)

    print(f"Data in root: {tree.root.data}")
    print(f"Color in root: {tree.root.color}")
    print(f"Data in left: {tree.root.left.data}")
    print(f"Color in left: {tree.root.left.color}")
    print(f"Data in right: {tree.root.right.data}")
    print(f"Color in right: {tree.root.right.color}")
    print(f"Deleted 20 {'-'*20}")
    tree.delete(20)
    print(f"Data in root: {tree.root.data}")
    print(f"Color in root: {tree.root.color}")
    print(f"Data in left: {tree.root.left.data}")
    print(f"Color in left: {tree.root.left.color}")
    print(f"Data in right: {tree.root.right.data}")
    print(f"Color in right: {tree.root.right.color}")
    tree.delete(10)
    tree.delete(30)
    print(f"Deleted 10 {'-'*20}")
    print(f"Deleted 30 {'-'*20}")
    print(f"Data in root: {tree.root.data}")

    d = [10, 5, 15, 1]
    for value in d:
        tree.insert(value)

    print(f"Inserted {d} {'-'*20}")
    print(f"Data in root: {tree.root.data}")
    print(f"Color in root: {tree.root.color}")
    print(f"Data in left: {tree.root.left.data}")
    print(f"Color in left: {tree.root.left.color}")
    print(f"Data in right: {tree.root.right.data}")
    print(f"Color in right: {tree.root.right.color}")
