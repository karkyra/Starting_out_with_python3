# Create a function to find only the root value of x in
# any quadratic equation ax^2 + bx + c. The function will take three arguments:
#     a as the coefficient of x^2
#     b as the coefficient of x
#     c as the constant term

import cmath

def quadratic_equation(a, b, c):

    dis = (b**2) - (4 * a*c)
    ans = (-b + cmath.sqrt(dis))/(2 * a)
    return round(ans.real, 1)


print(quadratic_equation(1, 2, -3))
print(quadratic_equation(2, -7, 3))
