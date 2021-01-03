# Create a function that takes two number strings and returns their sum as a string.

def add(n1, n2):

    if n1 == "" or n2 == "":
        return "Invalid Operation"
    else:
        return str(int(n1) + int(n2))


print(add("111", "111") )
print(add("", "20"))
print(add("10", "80"))
