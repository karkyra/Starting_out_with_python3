# Create a class that takes the following four arguments for
# a particular football player:
#     name
#     age
#     height
#     weight
# Also, create three functions for the class that returns the following strings:
#     get_age() returns "name is age age"
#     get_height() returns "name is heightcm"
#     get_weight() returns "name weighs weightkg"
class player():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return "{} is age {}".format(self.name, self.age)

    def get_height(self):
        return "{} is {}cm".format(self.name, self.height)

    def get_weight(self):
        return "{} weighs {}kg".format(self.name, self.weight)

p1 = player("David Jones", 25, 175, 75)
print(p1.get_age())

print(p1.get_height())
print(p1.get_weight())
