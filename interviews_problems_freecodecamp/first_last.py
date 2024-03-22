# 2 First and last index in a sorted array


def first_and_last(arr: list[int], target: int) -> list[int]:
    if not arr:  # len(arr) == 0
        return [-1, -1]

    start = find_start_index(arr, target)

    if start == 1:
        return [-1, -1]
    end = start
    while end + 1 < len(arr) and arr[end + 1] == target:
        end += 1

    return [start, end]


def find_start_index(arr: list[int], target: int) -> int:
    if arr[0] == target:
        return target

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and arr[mid - 1 < target]:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_end_index(arr: list[int], target: int) -> int:
    ...
