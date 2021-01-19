# Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.
# # GUEST_LIST = {
# "Randy": "Germany",
# "Karla": "France",
# "Wendy": "Japan",
# "Norman": "England",
# "Sam": "Argentina"
# }
#
# Write a function that takes in a name and returns a name tag, that should read:
#
# "Hi! I'm [name], and I'm from [country]."
#
# If the name is not in the dictionary, return:
#
# "Hi! I'm a guest."
GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}
def greeting(name):

    for k, v in GUEST_LIST.items():
        if k == name:
            return "Hi! I'm {}, and I'm from {}.".format(k, v)
    return "Hi! I'm a guest."

print(greeting("Randy"))
print(greeting("Sam"))
print(greeting("Monti"))
print(greeting("Wendy"))
