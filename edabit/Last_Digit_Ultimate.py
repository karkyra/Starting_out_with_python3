# Your job is to create a function, that takes 3 numbers: a, b, c and returns
# True if the last digit of a * b = the last digit of c. Check the examples below for an explanation.
def last_dig(a, b, c):

    total = a * b
    return str(total)[-1] == str(c)[-1]

print(last_dig(25, 21, 125))
print(last_dig(12, 215, 2142))
