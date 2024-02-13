# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def merge_sort(dataset: list) -> list:
    if len(dataset) > 1:
        print("Current dataset", dataset)
        midpoint = len(dataset) // 2
        left_array = dataset[:midpoint]
        right_array = dataset[midpoint:]

        # TODO: recursively break down the arrays
        merge_sort(left_array)
        merge_sort(right_array)

        # TODO: now perform the merging
        i_left = 0  # index into the left array
        i_right = 0  # index into the right array
        i_merged = 0  # index into merged array

        # TODO: while both arrays have content
        while i_left < len(left_array) and i_right < len(right_array):
            if left_array[i_left] < right_array[i_right]:
                dataset[i_merged] = left_array[i_left]
                print("Add from Left: ", dataset)
                i_left += 1
            else:
                dataset[i_merged] = right_array[i_right]
                print("Add from Right: ", dataset)
                i_right += 1

            i_merged += 1
        # TODO: if the left array still has values, add them
        while i_left < len(left_array):
            dataset[i_merged] = left_array[i_left]
            i_merged += 1
            i_left += 1

        # TODO: if the right array still has values, add them
        while i_right < len(right_array):
            dataset[i_merged] = right_array[i_right]
            i_merged += 1
            i_right += 1


# test the merge sort with data
print(items)
merge_sort(items)
print("Result ->", items)
