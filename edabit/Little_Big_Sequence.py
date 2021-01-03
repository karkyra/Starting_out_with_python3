# A number sequence is as follows:
# 5, 100, 6, 200, 7, 400, 8, 800, 9, 1600, 10, 3200, ...
# Given that 5 is at position 1, create a function that returns the number
# found at position n in the sequence.

def little_big(n):
	if n == 1:
		return 5
	if n % 2 != 0:
		return 5 + (n // 2)
	return 2**(n//2-1) * 100

print(little_big(4))
print(little_big(5))
print(little_big(28))
