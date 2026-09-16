"""
Given a list of numbers, return all the possible permutations of the elements, as well the
number os possible permutations calculated by its formula P(n).

P(n) = n!

O(n * P(n))
"""

from collections import deque


def permutations(nums: list[int]) -> tuple[int, list[list[int]]]:
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    if nums == []:
        return []

    length = len(nums)
    result: list[list[int]] = []
    possible_permutations = factorial(len(nums))  # n!
    queue = deque([([], set())])

    while queue:
        prefix, used_indexes = queue.popleft()

        # Check if is already a solution
        if len(prefix) == length:
            result.append(prefix)
            continue

        # Generate a new permutation and add to the queue
        for next_idx in range(len(nums)):
            if next_idx in used_indexes:
                continue

            # Add the new permutation
            new_prefix = prefix + [nums[next_idx]]
            queue.append((new_prefix, used_indexes | {next_idx}))

    return possible_permutations, result


if __name__ == "__main__":
    nums = [1, 2, 3]

    print(f"Permutations for {nums}: {permutations(nums)}")
