# Create a function that takes in a year and returns the correct century.
    # All years will be between 1000 and 2010.
    # The 11th century is between 1001 and 1100.
    # The 18th century is between 1701-1800.
from math import ceil
def century(year):
    cen = ceil(year / 100)
    suf = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))
    a = [suf(n) for n in range(1,22)]
    b = [i for i in range(1,22)]
    res = dict(zip(b, a))
    return "".join([v for k, v in res.items() if k == cen ]) + " century"


print(century(1756))
print(century(2005))
print(century(1555))
print(century(1000))
print(century(1001))
