# Given a number between 1-26, return what letter is at that position in the alphabet.
# Return "invalid" if the number given is not within that range, or isn't an integer.
    # Return a lowercase letter.
    # Numbers that end with ".0" are valid.
import string

def letter_at_position(n):

    # a = dict(zip(range(1,27), string.ascii_lowercase))
    # if n == 0:
    #     return "invalid"
    # elif int("".join([str(k) for k, v in a.items() if k == int(n)])) == n:
    #     return "".join([v for k, v in a.items() if k == int(n)])
    # else:
    #     return "invalid"

    if n == 0 or n != int(n):
        return "invalid"
    return chr(int(n)+96)


print(letter_at_position(1.0))
print(letter_at_position(26.0))
print(letter_at_position(4.5))
print(letter_at_position(0))
