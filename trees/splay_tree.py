class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


class SplayTree:
    def __init__(self):
        self.root: Node | None = None

    def _rotate_left(self, node: Node) -> None:
        child = node.right

        if child is None:
            return

        node.right = child.left

        if child.left:
            child.left.parent = node

        child.parent = node.parent

        if node.parent is None:
            self.root = child

        elif node == node.parent.left:
            node.parent.left = child

        else:
            node.parent.right = child

        child.left = node
        node.parent = child

    def _rotate_right(self, node: Node) -> None:
        child = node.left

        if child is None:
            return

        node.left = child.right

        if child.right:
            child.right.parent = node

        child.parent = node.parent

        if node.parent is None:
            self.root = child

        elif node == node.parent.left:
            node.parent.left = child

        else:
            node.parent.right = child

        child.right = node
        node.parent = child

    def _splay(self, node: Node) -> None:
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            # Zig
            if grandparent is None:
                if node == parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)

            # Zig-Zig: left-left
            elif node == parent.left and parent == grandparent.left:
                self._rotate_right(grandparent)
                self._rotate_right(parent)

            # Zig-Zig: right-right
            elif node == parent.right and parent == grandparent.right:
                self._rotate_left(grandparent)
                self._rotate_left(parent)

            # Zig-Zag: right-left
            elif node == parent.right and parent == grandparent.left:
                self._rotate_left(parent)
                self._rotate_right(grandparent)

            # Zig-Zag: left-right
            else:
                self._rotate_right(parent)
                self._rotate_left(grandparent)

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        parent = None

        while current:
            parent = current

            if value < current.value:
                current = current.left

            elif value > current.value:
                current = current.right

            else:
                self._splay(current)
                return

        new_node = Node(value)
        new_node.parent = parent

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._splay(new_node)

    def search(self, value: int) -> Node | None:
        current = self.root
        last = None

        while current:
            last = current

            if value == current.value:
                self._splay(current)
                return current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        # Common splay-tree behavior:
        # splay last accessed node even if value was not found.
        if last:
            self._splay(last)

        return None

    def minimum(self, node: Node) -> Node:
        current = node

        while current.left:
            current = current.left

        return current

    def maximum(self, node: Node) -> Node:
        current = node

        while current.right:
            current = current.right

        return current

    def print_inorder(self) -> None:
        stack: list[Node] = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.value, end=" ")

            current = current.right

        print()


if __name__ == "__main__":
    tree = SplayTree()

    for value in [10, 20, 30, 40, 50, 25]:
        tree.insert(value)

        print(f"Inserted {value}, " f"root = {tree.root.value}")

    print()

    tree.print_inorder()

    print("\nSearch 20")
    tree.search(20)

    print("New root:", tree.root.value)

    print("\nSearch 10")
    tree.search(10)

    print("New root:", tree.root.value)
