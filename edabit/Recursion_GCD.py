# Write a function that calculates the GCD (Greatest Common Divisor) of two numbers recursively.

def gcd(a, b):

    if a > b:
        small = b
    else:
        small = a

    for i in range(1, small + 1):
        if ((a % i == 0) and (b % i ==0 )):
            g = i

    return g

print(gcd(10, 20))
print(gcd(5, 7))
