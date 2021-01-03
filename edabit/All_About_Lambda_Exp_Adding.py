# Write a function that returns a lambda expression, which adds n to its input

def adds_n(n):
    return lambda x: x+n

adds1 = adds_n(1)
print((adds1))
