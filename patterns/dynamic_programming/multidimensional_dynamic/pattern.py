"""
Dynamic programming.

MAIN PROBLEM: Understand what is the size of the dynamic and what
to store inside the DP.

Time: O(w*n)
Memory: O(n*w)
"""


def knapack(weights: list[int], values: list[int], capacity: int) -> int:
    # =============================================================================
    # Initialization
    # =============================================================================
    n: int = len(weights)
    dp: list[list[int]] = [[0] * (capacity + 1) for _ in range(n)]

    # =============================================================================
    # Base cases (if needed)
    # =============================================================================
    ...

    # =============================================================================
    # Obtaining the next values with recursion
    # =============================================================================
    for i in ...:
        ...

    return dp[n][capacity]
