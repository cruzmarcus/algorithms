# use a hash table to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = [
    "apple",
    "pear",
    "orange",
    "banana",
    "apple",
    "orange",
    "apple",
    "pear",
    "banana",
    "orange",
    "apple",
    "kiwi",
    "pear",
    "apple",
    "orange",
]

filtering = {item: 0 for item in items}

# create a set from the resulting keys in the hash table
result = set(filtering.keys())
print(result)
