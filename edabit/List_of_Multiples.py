# Create a function that takes two numbers as arguments (num, length)
# and returns a list of multiples of num until the
# list length reaches length.

def list_of_multiples (num, length):

    lst =[]
    n = num
    for i in range(1, length+1):
        lst.append(num)
        num += n
    return lst

print(list_of_multiples(7, 5))
