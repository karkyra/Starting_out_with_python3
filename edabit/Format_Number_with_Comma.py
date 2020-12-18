# Create a function that takes a number as an argument and
# returns a string formatted to separate thousands.

def format_num(n):


    return str("{:,}".format(n))
    # return str(a)


print(format_num(100000))
print(format_num(1000))
print(format_num(20))
