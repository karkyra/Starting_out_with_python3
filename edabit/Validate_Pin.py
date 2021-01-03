# Create a function to test if a string is a valid pin or not.
# A valid pin has:
#     Exactly 4 or 6 characters.
#     Only numerical characters (0-9).
#     No whitespace.
# Empty strings should return False when tested.
def valid(txt):
    return (txt.isdigit() and len(txt) ==4) or (txt.isdigit() and len(txt) ==6)

print(valid("1234"))
print(valid("45135"))
print(valid("89abc1"))
print(valid("900876"))
print(valid(" 4983") )
