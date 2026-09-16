from collections import deque


def n_choose_k(nums: list[int], k: int) -> tuple[int, list[list[int]]]:
    """
    Given an array of integers, give me all the possible combinations of k elements, and say how much there are.

    C(n,k) = n!/(k! * (n-k)!)

    We can use backtracking to solve this problem:

    We can explore all the possibilities creating something like a tree, but using queues.
    Since those are combinations, we use each element with all he rest of others,
    so we will be doying something like prefix sum but with the elements.

    The O(k * C(n,k))

    THE ORDER OF ELEMENTS DOES NOT MATTER, SO (A,B) IS THE SAME AS (B,A)
    """

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    if k > len(nums) or nums == []:
        return -1

    result: list[list[int]] = []
    queue: deque[tuple[str, int]] = deque([("", 0)])
    max_combinations: int = factorial(len(nums)) / (
        factorial(k) * factorial(len(nums) - k)
    )

    while (
        queue and len(queue[0][0]) < k
    ):  # O(C(n, k)) since we need to get all the combinations
        prefix, curr_index = queue.popleft()

        # Add all the remaining possible combinations of this branch for the given prefix
        for i in range(curr_index, len(nums)):
            new_prefix = prefix + str(nums[i])
            # Add to the queue
            queue.append([new_prefix, i + 1])
            if len(new_prefix) == k:  # O(k) just to construct the output
                result.append(new_prefix)

    return max_combinations, result


if __name__ == "__main__":
    # Example:
    nums = [3, 5, 7, 8]
    k = 3
    print(f"Combinations for {nums} and k = {k}: {n_choose_k(nums, k)}")
    print(f"Combinations for {nums} and k = {2}: {n_choose_k(nums, 2)}")
