def binary_sort(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    if not arr:
        return -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    arr: int = [1, 2, 3, 4, 5, 6, 7, 11, 15, 55, 100]
    tg1: int = 15
    tg2: int = 10

    assert binary_sort(arr, tg1) == 8
    assert binary_sort(arr, tg2) == -1
    assert binary_sort([], tg2) == -1

    print("All tests passed!")
