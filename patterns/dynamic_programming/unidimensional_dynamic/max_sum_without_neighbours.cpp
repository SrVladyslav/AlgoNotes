/**
 * Given an array of nummbers nums. We should find the maximum sum of numbers,
 * if we can't sum two neighbours.
 *
 * e.g.
 * nums = [1,3,1,1,9,1]
 * solution = 12
 *
 * E
 */

#include <iostream>
#include <vector>

using namespace std;

int max_sum_without_neighbours(vector<int> nums)
{
    vector<int> dp(nums.size(), 0);

    dp[0] = nums[0];
    dp[1] = max(nums[1], nums[0]);

    for (int i = 2; i < nums.size(); i++)
    {
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
    }

    return dp[dp.size() - 1];
}

int main()
{
    vector<int> nums = {1, 3, 1, 1, 9, 1};
    printf("Result: %d\n", max_sum_without_neighbours(nums));

    return 0;
}