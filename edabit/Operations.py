# Write a function that does the following things: adding, subtracting,
# dividing, or multiplying values. It is simply referred to as variable
# operation variable. Of course, the variables have to be defined, but
# in this challenge, the variable will be defined for you. All you have
#  to do is look at the variable, do some string to integer conversions
#use some if conditionals, and combine them based on the operation.

# The numbers and operation will be given as a string, and you should
#return the value as a string as well.

def operation(a, b, op):


    oper = {"add":"+", "subtract": "-", "divide": "/", "multiply": "*"}
    try:
        return  str(round(eval(a + oper.get(op) + b)))
    except ZeroDivisionError:
        return "undefined"


print(operation("1", "2", "add" ) )
print(operation("4", "5", "subtract"))
print(operation("6", "3", "divide") )
print(operation("9", "0", "divide"))
