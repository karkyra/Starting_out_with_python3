# Create a function that takes a number num and returns its length.
# DO NOT USE LEN() FOR THIS CHALLENGE
def number_length(num):

    num = str(num)
    total = 0

    for i in num:
        total +=1
    return total


print(number_length(10))
