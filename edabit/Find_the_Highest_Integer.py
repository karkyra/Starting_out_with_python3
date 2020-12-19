# Create a function that finds the highest integer in the list using recursion.
# Please use the recursion to solve this (not the max() method).

def find_highest(lst):
    # return sorted(lst)[-1]

    if len(lst) == 1:
        return lst[0]
    else:
        current = find_highest(lst[1:])
        return current if current > lst[0] else lst[0]

print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
print(find_highest([8]))
