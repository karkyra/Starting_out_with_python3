
def is_prime(n):
    if n <= 1 or n % 1 > 0:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

print(is_prime(3))
print(is_prime(6))
