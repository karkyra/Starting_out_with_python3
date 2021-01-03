# Create methods for the Calculator class that can do the following:
#     Add two numbers.
#     Subtract two numbers.
#     Multiply two numbers.
#     Divide two numbers.

class Calculator:
	# Write methods to add(), subtract(), multiply() and divide()
    def __init__(self):
        pass
    def add(self, x, y):
        return   x + y


    def subtract(self, x, y):
        return x - y


    def multiply(self, x, y):
        return x * y


    def divide(self, x, y):
        return x / y

calculator = Calculator()

print(calculator.add(10, 5))
