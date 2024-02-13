# searching for an item in an unordered list
# sometimes called a Linear Search

# declare a list od values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(item: int, item_list: list[int]) -> int | None:
    for index in range(len(item_list)):
        if item == item_list[index]:
            return index

    return None

    # return next(
    #     (index for index in range(len(item_list)) if item_list[index] == item), None
    # )


print(find_item(87, items))
print(find_item(250, items))
