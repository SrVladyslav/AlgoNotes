"""
Given a value n, which represents the number of steps in a staircase, in each
step you can either climb 1 or 2 steps. You should return the number of different
ways to climb to the top.

e.g.
n = 5
result = 8
"""


def ways_to_climb(n: int) -> int:
    if n <= 0:
        return -1
    # Stage 1: Init the DP array
    dp: list[int] = [0] * (n + 1)

    # Stage 2: Process the base cases
    dp[0] = 1
    dp[1] = 1

    # Stage 3: Process the relations recursively
    for i in range(2, n + 1):
        # Here we only need the previous and the previous to that from the case statement
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n: int = 5
    print(f"Result for n = {n}: {ways_to_climb(n)}")
