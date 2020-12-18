# Create a function that takes two arguments: the original price and the discount percentage
# as integers and returns the final price after the discount.

def dis(price, discount):

    a = price - (price * discount /100)

    return round(a, 2)

print(dis(89, 20) )
print(dis(100, 75))
