# Create a function that changes all the elements in a list as follows:
#
#     Add 1 to all even integers, nothing to odd integers.
#     Concatenates "!" to all strings and make the first letter of the word a capital letter.
#     Changes all boolean values to its opposite.
    # There won't be any float values.
    # You won't get strings with both numbers and letters in them.
    # Although the task may be easy, try keeping your code as clean and as readable as possible!

def change_types(lst):

    lst2 = []
    for i in lst:
        if type(i) == int and i % 2 == 0:
            lst2.append(i +1)
        elif type(i) == str:
            lst2.append(i.capitalize()+"!")
        elif i == True:
            lst2.append(False)
        elif i == False:
            lst2.append(True)
        else:
            lst2.append(i)

    print(lst2)


change_types(["a", 12, True])
change_types([13, "13", "12", "twelve"])
