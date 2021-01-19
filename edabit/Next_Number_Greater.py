# You are given two numbers a and b. Create a function that returns the next number
# greater than a and b and divisible by b.
def divisible_by_b(a, b):

    c = (a + b) % b

    if c == 0:
        return a
    else:
        return a + b - c

print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3) )
