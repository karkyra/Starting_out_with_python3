# Write a function that inverts the keys and values of a dictionary.

def invert(dct):

    return dict(zip(dct.values(), dct.keys()))


print(invert({ "z": "q", "w": "f" }))
