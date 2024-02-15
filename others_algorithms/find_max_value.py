# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_max(items):
    # TODO: breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # TODO: otherwise get the first item and call function
    # again to operate on the rest of the list
    num1 = items[0]
    print("Num 1: ", num1)
    num2 = find_max(items[1:])
    print("Num 2: ", num2)

    # TODO: perform the comparison when we're down to just two
    if num1 > num2:
        return num1
    else:
        return num2


# test the function
print(find_max(items))
