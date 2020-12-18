import re


def validate(s):
    x = "^[0-9]{5}$"
    return bool(re.match(x, s))

# x = re.search(r"[0-9]{5}", s)

print(validate("81442"))
print(validate("9a345"))
print(validate("%2345"))
print(validate("933345"))
