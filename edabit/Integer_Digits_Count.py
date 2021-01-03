# Create a function that counts the integer's number of digits.
def count(n):

    return len(str(abs(n)))

print(count(318))
print(count(-92563))
