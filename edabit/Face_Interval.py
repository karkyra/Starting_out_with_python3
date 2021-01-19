# In mathematics, interval is the difference between the largest number and the smallest number in a list.
# To illustrate:
# A = (3, 5, 7, 23, 11, 42, 80)
# Interval of A = 80 - 3 = 77
# Create a function that takes a list and returns ":)" if the interval of the list is equal
#  to any other element; otherwise return ":(".
#      Lists won't contain any duplicate numbers.
#     If you're not given a list, return ":/"
def face_interval(num):

    # total = max(num) - min(num)

    if type(num) is not list:
        return ":/"
    elif max(num) - min(num) in num:
        return ":)"
    else:
        return ":("


print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval("bruh"))
