class State:
    def __init__(self):
        self.next: dict[str, int] = {}
        self.link: int = -1
        self.length: int = 0


class SuffixAutomaton:
    def __init__(self):
        self.states = [State()]
        self.last = 0

    def extend(self, char: str) -> None:
        current = len(self.states)
        self.states.append(State())

        self.states[current].length = self.states[self.last].length + 1

        p = self.last

        # Add transitions for char while they don't exist
        while p != -1 and char not in self.states[p].next:
            self.states[p].next[char] = current
            p = self.states[p].link

        if p == -1:
            # We reached the root
            self.states[current].link = 0

        else:
            q = self.states[p].next[char]

            # Simple case:
            # q extends p by exactly one character
            if self.states[p].length + 1 == self.states[q].length:
                self.states[current].link = q

            else:
                # Need a clone
                clone = len(self.states)
                self.states.append(State())

                self.states[clone].length = self.states[p].length + 1
                self.states[clone].next = self.states[q].next.copy()
                self.states[clone].link = self.states[q].link

                # Redirect transitions to the clone
                while p != -1 and self.states[p].next.get(char) == q:
                    self.states[p].next[char] = clone
                    p = self.states[p].link

                self.states[q].link = clone
                self.states[current].link = clone

        self.last = current

    def build(self, text: str) -> None:
        for char in text:
            self.extend(char)

    def longest_common_substring(self, text: str) -> int:
        state = 0
        current_length = 0
        max_length = 0

        for char in text:

            # If transition doesn't exist,
            # follow suffix links until it does
            while state != 0 and char not in self.states[state].next:
                state = self.states[state].link
                current_length = self.states[state].length

            # Can continue the substring
            if char in self.states[state].next:
                state = self.states[state].next[char]
                current_length += 1

            else:
                # Even root has no transition
                state = 0
                current_length = 0

            max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":

    s1 = "abcfgh"
    s2 = "acdghr"

    automaton = SuffixAutomaton()
    automaton.build(s1)

    result = automaton.longest_common_substring(s2)

    print(result)  # 2
