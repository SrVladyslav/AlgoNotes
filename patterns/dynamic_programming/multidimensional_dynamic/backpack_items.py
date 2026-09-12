"""
Given a backpack of size 6, and a set of items with weight and price.
Find the maximum value of the items that can be put into the backpack.
Every item you can put it into the backpack is just one time.

Example:
w = 6
items:[weight, price] = [(5,6), (3,4), (2,3)]


Solution: 7 -> (second and last item)



   0  1  2  3  4  5  6  remaining backpack size
0  0  0  0  0  0  0  0
1  0  0  0  0  0  6  6
2  0  0  0  4  4  6  6
3  0  0  3  4  4  7  7
^- quantity of first items we will be putting inside the backpack


And the dp[x,y] shows the maximum size of the items we can put inside the backpack

When we go with the first one, we see, can we put the first element of the array
into the backpack? It has the weight of 5, so the next 4 wil be 0.
Then we note in th e5th position its price,
The 2 row, until 2 there are 0, since we can't fit the 3 inside, in the 3rd,
we can fit it, we need to get the maxium of two options:
1) We don't get the value, then we check the row up of it, which is 0.
2) We get the item 2 with weight 3, since we are at 3rd remaining size, 3-3 = 0,
then we check the previous objects for 0, which is dp[0][2-1] -> 0+4 = 4 and finally
the max(0, 4) => 4
"""


# In every cicle we choose to take or not the element
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    items_length: int = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(items_length + 1)]

    for i in range(1, items_length + 1):
        for weight in range(capacity + 1):
            if weights[i - 1] <= weight:
                dp[i][weight] = max(
                    dp[i - 1][weight],
                    values[i - 1] + dp[i - 1][weight - weights[i - 1]],
                )
            else:
                dp[i][weight] = dp[i - 1][weight]
    return dp[items_length][capacity]


def knapsack_optimized(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        for new_weight in range(capacity, weight - 1, -1):
            dp[new_weight] = max(new_weight, dp[new_weight - weight] + value)

    return dp[capacity]


if __name__ == "__main__":
    weights: list[int] = [5, 3, 2]
    values: list[int] = [6, 4, 3]
    capacity: int = 6

    print(f"The maximum value of the items is: {knapsack(weights, values, capacity)}")
    print(
        f"The maximum OPT value of the items is: {knapsack_optimized(weights, values, capacity)}"
    )
