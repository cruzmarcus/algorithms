# searching for an item in an ordered list
# this technique uses a BINARY SEARCH

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binary_search(value: int, item_list: list[int]) -> int | None:
    # get the list size
    list_size = len(item_list) - 1

    # start at the two ends of the list
    lower_index = 0
    upper_index = list_size

    while lower_index <= upper_index:
        # calculate the middle point
        midpoint = (lower_index + upper_index) // 2

        # if item is found, return the index
        if item_list[midpoint] == value:
            return midpoint

        # otherwise get the next midpoint
        if value > item_list[midpoint]:
            lower_index = midpoint + 1
        else:
            upper_index = midpoint - 1

    if lower_index > upper_index:
        return None


print(binary_search(23, items))
print(binary_search(87, items))
print(binary_search(230, items))
