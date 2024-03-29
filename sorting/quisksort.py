# Implement a quicksort


def quick_sort(dataset: list, first: int, last: int) -> list:
    if first < last:
        # calculate the split point
        pivot_index = partition(dataset, first, last)

        # now sort the two partitions
        quick_sort(dataset, first, pivot_index - 1)
        quick_sort(dataset, pivot_index + 1, last)


def partition(data_values: list, first: int, last: int) -> list:
    # choose the first item as the picot value
    pivot_value = data_values[first]

    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    done = False
    while not done:
        # advance the lower index
        while lower <= upper and data_values[lower] <= pivot_value:
            lower += 1

        # advance the upper index
        while data_values[upper] >= pivot_value and upper >= lower:
            upper -= 1

        # if the two indexes cross, wht have found the split point
        if upper < lower:
            done = True
        else:
            temp = data_values[lower]
            data_values[lower] = data_values[upper]
            data_values[upper] = temp

    # when the split point is found, exchange the picot value
    temp = data_values[first]
    data_values[first] = data_values[upper]
    data_values[upper] = temp

    # return the split point index
    return upper


# test the merge sort with data
items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]

print(items)
quick_sort(items, 0, len(items) - 1)
print(items)
