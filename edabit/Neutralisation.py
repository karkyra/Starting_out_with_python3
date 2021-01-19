# Given two strings comprised of + and -, return a new string which shows how the two
#strings interact in the following way:
#     When positives and positives interact, they remain positive.
#     When negatives and negatives interact, they remain negative.
#     But when negatives and positives interact, they become neutral, and are shown as the number 0.

# neutralise("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.

def neutralise(s1, s2):


    lst = [0 if i != j else i for i, j in zip(s1, s2)]
    return ''.join([str(elem) for elem in lst])

print(neutralise("--++--", "++--++") )
print(neutralise("-+-+-+", "-+-+-+"))
print(neutralise("-++-", "-+-+"))
