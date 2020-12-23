#A man has n number of apples. If he eats a percentage p of the apples
#(if apples are available), his children will share the remainder of the apples.
#Create a function to determine the number of 'whole' apples his children got.
#If his children did not get any apples, return "The children didn't get any apples".
import math
def get_number_of_apples(n, p):

    percentage = p.split("%")
    if n == 0 or int(percentage[0]) ==100:
        return "The children didn't get any apples"
    else:
        return n - math.ceil(n*int(percentage[0])/100)


print(get_number_of_apples(10, "90%"))
print(get_number_of_apples(25, "10%"))
print(get_number_of_apples(0, "10%"))
