def merge_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    def _merge(left: list[int], right: list[int]) -> list[int]:
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if i < len(left):
            result.extend(left[i:])
            i += 1

        if j < len(right):
            result.extend(right[j:])

        return result

    def _merge_sort(arr: list[int]) -> list[int]:
        left = 0
        right = len(arr)
        if not arr:
            return []

        if len(arr) == 1:
            return arr

        middle = left + (right - left) // 2

        first_part = _merge_sort(arr[left:middle])
        second_part = _merge_sort(arr[middle:right])
        return _merge(first_part, second_part)

    return _merge_sort(arr)


if __name__ == "__main__":
    arr: list[int] = [5, 2, 6, 1, 3, 4, 7]
    assert merge_sort(arr) == [1, 2, 3, 4, 5, 6, 7]

    print("All tests passed!")
