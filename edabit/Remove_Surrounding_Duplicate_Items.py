# Create a function that takes a sequence of either strings or integers,
# removes the surrounding duplicates and returns a list of items without
# any items with the same value next to each other and preserves the original order of items.
    # The initial sequence of items can be either a string or a list.
    # Tests are case sensitive.
from itertools import groupby
def unique_in_order(sequence):

    # return [v for i, v in enumerate(sequence) if i == 0 or v != sequence[i-1]]
    return [x[0] for x in groupby(sequence) ]

print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order("ABBCcAD"))
print(unique_in_order([1, 2, 2, 3, 3]))
