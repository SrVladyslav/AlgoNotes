class KMP:
    # Searches for a pattern inside a text.

    def __init__(self, pattern: str):
        self.pattern = pattern
        self.lps: list[int] = self.build_lps()

    def build_lps(self) -> list[int]:
        """
        Builds the LPS array.

        LPS[i] = length of the longest proper prefix of pattern[:i+1]
        which is also a suffix.
        """
        lps = [0] * len(self.pattern)

        length = 0
        i = 1

        while i < len(self.pattern):
            if self.pattern[i] == self.pattern[length]:
                length += 1
                lps[i] = length
                i += 1

            elif length > 0:
                # Try a smaller prefix
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

        return lps

    def search(self, text: str) -> int:
        """
        Returns the index of the first occurrence of pattern in text.
        Returns -1 if not found.

        Time:  O(n + m)
        Space: O(m)
        """
        if not self.pattern:
            return 0

        i = 0  # text pointer
        j = 0  # pattern pointer

        while i < len(text):

            if text[i] == self.pattern[j]:
                i += 1
                j += 1

                if j == len(self.pattern):
                    return i - j

            elif j > 0:
                # Don't move i.
                # Reuse what we already know about the pattern.
                j = self.lps[j - 1]

            else:
                i += 1

        return -1


if __name__ == "__main__":
    s1 = "xxxxabcfghyyyy"
    s2 = "abcfgh"
    kmp = KMP(s2)
    print(f"KMP Built: {kmp.lps}")

    print(f"The solution for {s1} is in index: {kmp.search(s1)}")
