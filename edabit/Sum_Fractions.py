# Create a function that takes a list containing nested lists as an argument.
# Each sublist has 2 elements. The first element is the numerator and the second
# element is the denominator. Return the sum of the fractions rounded to the nearest whole number.

def sum_fractions(lst):

    return round(sum([i[0] / i[1] for i in lst]))

print(sum_fractions([[18, 13], [4, 5]]))
print(sum_fractions([[36, 4], [22, 60]]))
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))
