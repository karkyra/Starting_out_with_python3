# In this challenge, you have to establish if a given integer n is a Sastry number.
#If the number resulting from the concatenation of an integer n with its successor
#is a perfect square, then n is a Sastry Number.
#
# Given a positive integer n, implement a function that returns True if n is a Sastry
#number, or False if it's not.
# is_sastry(183) ➞ True
# Concatenation of n and its successor = 183184
# 183184 is a perfect square (428 ^ 2)
import math
def is_sastry(n):

    num = str(n) + str(n+1)
    sr = math.sqrt(int(num))
    print(sr)
    print(int(sr))

print(is_sastry(183))
print(is_sastry(184))
print(is_sastry(106755))
print(is_sastry(129987253440921))
