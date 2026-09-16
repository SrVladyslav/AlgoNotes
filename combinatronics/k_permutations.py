"""
Given a list of integers, and a number k, return all the possible permutations of k elements and the queantity of possible permutations.

P(n,k) = n! / (n-k)!

THE ORDER OF THE ELEMENTS DOES MATTER, SO (A,B) IS NOT THE SAME AS (B,A)

O(n * P(n,k))
"""

from collections import deque


def k_permutations(nums: list[int], k: int) -> tuple[int, list[list[int]]]:
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    if k > len(nums) or nums == []:
        return -1

    result: list[list[int]] = []
    possible_permutations = factorial(len(nums)) / (factorial(len(nums) - k))

    # We will use the set to know which stuff we already used and which not
    queue = deque([([], set())])  # Storing (surrent_prefix, used_indexes of elements)

    while queue:
        prefix, used = queue.popleft()

        if len(prefix) == k:
            result.append(prefix)
            continue

        for i in range(len(nums)):
            if i in used:
                continue

            new_prefix = prefix + [nums[i]]
            new_used = used | {i}
            queue.append((new_prefix, new_used))

    return possible_permutations, result


if __name__ == "__main__":
    # Example:
    nums = [3, 5, 7]
    k = 3
    print(f"Combinations for {nums} and k = {k}: {k_permutations(nums, k)}")
    print(f"Combinations for {nums} and k = {2}: {k_permutations(nums, 2)}")
