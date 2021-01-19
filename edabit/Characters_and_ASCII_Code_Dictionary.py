# Write a function that transforms a list of characters into a list of dictionaries, where:
#
#     The keys are the characters themselves.
#     The values are the ASCII codes of those characters.

# example to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

def to_dict(lst):

    return [{i: ord(i)} for i in lst]

print(to_dict(["a", "b", "c"]))
print(to_dict(["^"]) )
print(to_dict([]))
print(to_dict([" "]))
