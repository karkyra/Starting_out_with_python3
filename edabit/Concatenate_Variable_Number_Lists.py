# Create a function that concatenates n input lists, where n is variable.

def concat(*args):
    return [ j for i in args for j in i]



print(concat([1, 2, 3], [4, 5], [6, 7]))
print(concat([1], [2], [3], [4], [5], [6], [7]))
print(concat([4, 4, 4, 4, 4]))
