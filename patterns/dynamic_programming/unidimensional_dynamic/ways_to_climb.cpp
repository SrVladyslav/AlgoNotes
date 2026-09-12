/**
Given a value n, which represents the number of steps in a staircase, in each
step you can either climb 1 or 2 steps. You should return the number of different
ways to climb to the top.

e.g.
n = 5
result = 8
 */

#include <vector>
#include <iostream>

using namespace std;

int ways_to_climb(int n)
{
    // Edge cases
    if (n <= 0)
        return -1;

    // Stage 1: Init the Dynamic programming
    vector<int> dp(n + 1, 0);

    // Stage 2: Set the base cases
    dp[0] = 1;
    dp[1] = 1;

    // Creating the array of the relations
    for (int i = 2; i < n + 1; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

// Time: O(n), Memory: O(1)
int ways_to_climb_optimized(int n)
{
    if (n <= 0)
        return -1;

    int prev1 = 1;
    int prev2 = 1;

    for (int i = 2; i <= n; i++)
    {
        int current = prev1 + prev2;
        prev1 = prev2;
        prev2 = current;
    }
    return prev2;
}

int main()
{
    int n = 5;

    printf("Result for n = %d: %d\n", n, ways_to_climb(n));
    printf("OPT Result for n = %d: %d\n", n, ways_to_climb_optimized(n));
    return 0;
}