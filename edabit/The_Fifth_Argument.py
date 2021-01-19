# Create a function (named fifth) that takes some arguments and returns the type of the fifth argument.
#  In case the arguments were less than 5, return "Not enough arguments".

def fifth(*n):

    try:
        return type(n[4]).__name__
    except IndexError:
        return "Not enough arguments"


print(fifth(1, 2, 3, 4, 5))
print(fifth("a", 2, 3, [1, 2, 3], "five"))
print(fifth(1,2,3,4))
print(fifth())
