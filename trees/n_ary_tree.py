from collections import deque


class NaryNode:
    def __init__(self, value: int):
        self.value = value
        self.children: list[NaryNode] = []


class NaryTree:
    def __init__(self):
        self.root: NaryNode | None = None

    def insert(self, value: int, parent_value: int | None = None) -> None:
        new_node = NaryNode(value)

        # First node becomes root
        if self.root is None:
            self.root = new_node
            return

        if parent_value is None:
            raise ValueError("parent_value is required if tree is not empty")

        parent: NaryNode = self.search(parent_value)
        if parent is None:
            raise ValueError(f"Node {parent_value} not found")

        parent.children.append(new_node)

    def search(self, value: int) -> NaryNode | None:
        if self.root is None:
            return None

        stack: deque[NaryNode] = deque([self.root])

        while stack:
            node = stack.pop()
            # Base case
            if node.value == value:
                return node

            # Check for the children
            for child in reversed(node.children):
                stack.append(child)

        return None

    def dfs(self) -> list[int]:
        if self.root is None:
            return []

        result: list[int] = []
        stack: deque[NaryNode] = deque([self.root])

        while stack:
            node: NaryNode = stack.pop()
            result.append(node.value)

            # Explore the children, also reverse because stack is LIFO
            for child in reversed(node.children):
                stack.append(child)

        return result

    def bfs(self) -> list[int]:
        if self.root is None:
            return []

        result: list[int] = []
        queue: deque[NaryNode] = deque([self.root])

        while queue:
            node: NaryNode = queue.popleft()
            result.append(node.value)

            for child in node.children:
                queue.append(child)

        return result

    def print_levels(self) -> None:
        if self.root is None:
            print("Empty tree")
            return

        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.value)

                for child in node.children:
                    queue.append(child)

            print(level)


if __name__ == "__main__":

    """ 
            1
         /  |  \\
        2   3   4
       / \\    /|\\
      5   6   7 8 9
    """
    tree = NaryTree()

    tree.insert(1)

    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 1)

    tree.insert(5, 2)
    tree.insert(6, 2)

    tree.insert(7, 4)
    tree.insert(8, 4)
    tree.insert(9, 4)

    tree.print_levels()

    print("DFS:", tree.dfs())
    print("BFS:", tree.bfs())

    node = tree.search(8)

    if node:
        print("Found:", node.value)
