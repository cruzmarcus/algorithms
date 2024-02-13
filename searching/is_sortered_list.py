# determine if a list is sorted

item1 = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
item2 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def is_sorted(item_list):
    # for i in range(len(item_list) - 1):
    #     if item_list[i] > item_list[i + 1]:
    #         return False

    # return True
    return all(item_list[i] <= item_list[i + 1] for i in range(len(item_list) - 1))


print(is_sorted(item1))
print(is_sorted(item2))
