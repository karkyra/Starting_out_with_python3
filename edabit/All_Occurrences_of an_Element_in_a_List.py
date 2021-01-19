# Create a function that returns the indices of all occurrences of an item in the list.
#     If an element does not exist in a list, return [].
#     Lists are zero-indexed.
#     Values in the list will be value-types (don't need to worry about nested lists).

def get_indices(lst, el):

    return [i for i, j in enumerate(lst) if j == el]

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices([1, 5, 5, 2, 7], 5))
print(get_indices([1, 5, 5, 2, 7], 8))
