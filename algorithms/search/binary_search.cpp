#include <iostream>
#include <vector>

using namespace std;

int binary_search(const vector<int> &arr, int target)
{
    int left = 0;
    int right = arr.size() - 1;

    if (arr.empty())
        return -1;

    while (left <= right)
    {
        int middle = left + (right - left) / 2;

        if (arr[middle] == target)
        {
            return middle;
        }
        else if (
            arr[middle] < target)
        {
            left = middle + 1;
        }
        else
        {
            right = middle - 1;
        }
    }

    return -1;
}

int main()
{
    vector<int> arr{1, 2, 3, 4, 5, 6, 7, 11, 15, 55, 100};
    vector<int> void_vector{};
    int target1 = 15;
    int target2 = 10;

    cout << "Target 1: " << binary_search(arr, target1) << endl;
    cout << "Target 2: " << binary_search(arr, target2) << endl;
    cout << "Target 3: " << binary_search(arr, 0) << endl;
    cout << "Target 4: " << binary_search(void_vector, 1000) << endl;

    return 0;
}