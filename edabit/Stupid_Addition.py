# Create a function that takes two parameters and, if both parameters are strings,
# add them as if they were integers or if the two parameters are integers, concatenate them.
    # If the two parameters are different data types, return None.
    # All parameters will either be strings or integers.

def stupid_addition(a, b):


    if type(a) == int and type(b) == int:
        return str(a) + str(b)
    elif type(a) == str and type(b) == str:
        return int(a) + int(b)
    else:
        return None
        # if (type(a) == int and type(b) == str) or (type(a) == str and type(b) == int ):
        #     return None

print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))
