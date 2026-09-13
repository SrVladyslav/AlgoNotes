class TrieNode:
    def __init__(self, is_end: bool = False):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = is_end


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def _find(self, word: str) -> TrieNode | None:
        node: TrieNode = self.root

        for char in word:
            if char not in node.children:
                return None

            node = node.children[char]

        return node

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node: TrieNode | None = self._find(word=word)
        return (
            node is not None and node.is_end
        )  # If is not end, then the world does not exist and its a prefix

    def starts_with(self, prefix: str) -> bool:
        node: TrieNode | None = self._find(word=prefix)
        return node is not None


if __name__ == "__main__":
    trie = Trie()

    print(f"Searching for cat with root node: {trie.search('cat')}")
    print("Inserting cat")
    trie.insert("cat")
    print(f"Searching for cat: {trie.search('cat')}")
    print(f"Searching for ca: {trie.search('ca')}")
    print(f"Starting with ca: {trie.starts_with('ca')}")
    print(f"Starting with dog: {trie.starts_with('dog')}")
    print("Inserting car")
    trie.insert("car")
    print(f"Searching for car: {trie.search('car')}")
    print(f"Searching for cat: {trie.search('cat')}")
