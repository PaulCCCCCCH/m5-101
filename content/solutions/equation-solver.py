# -*- coding: utf-8 -*-
'''
Author: Chonghan Chen (paulcccccch@gmail.com)
-----
Last Modified: Thursday, 18th March 2021 3:06:59 pm
Modified By: Chonghan Chen (paulcccccch@gmail.com)
-----
Copyright (c) 2021 IceWould Information Technology Co., Ltd.
'''
import math

#################
### Section 1 ###
#################
def solve_linear(a, b):
    """
    求解方程　ax + b = 0
    """
    if a == 0 and b == 0:
        return None
    elif a == 0:
        return []
    else: return [-b / a]

#################
### Section 2 ###
#################
def solve_with_formula(a, b, c):
    """
    求解方程　ax^2 + bx + c = 0
    """
    if a == 0:
        return solve_linear(b, c)

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return []
    elif delta == 0:
        return [-b / (2*a)]
    else:
        delta_sqrt = delta ** 0.5
        return [(-b + delta_sqrt) / (2*a), (-b - delta_sqrt) / (2*a)]

#################
### Section 3 ###
#################
def d(f):
    return lambda x: (f(x + 1e-6) - f(x)) / 1e-6

def solve_equation(f):
    """
    求解方程 f = 0
    """

    xi = 1
    while abs(f(xi)) > 1e-6:
        xi = xi - f(xi)/d(f)(xi)
    return xi


if __name__ == "__main__":
    import math
    f = lambda x: math.exp(1) ** (60 * x) - 1000 * x - 1
    print(solve_equation(f))

    print("正在检查 Section 1：")
    assert(solve_linear(3, 6) == [-2])
    assert(abs(solve_linear(3, 4)[0] + 4 / 3) < 1e-6)
    assert(solve_linear(0, 5) == [])
    assert(solve_linear(5, 0) == [0])
    assert(solve_linear(0, 0) == None)
    print("Section 1 正确")

    print("正在检查 Section 2：")
    assert(solve_with_formula(1, 2, 1) == [-1])
    assert(solve_with_formula(3, 2, 1) == [])

    sol = solve_with_formula(4, 5, -6)
    # print(sol)
    # assert(sol + 5 / 4 < 1e-6)
    assert(abs(sol[0] + sol[1] + 5 / 4) < 1e-6)
    assert(abs(sol[0] * sol[1] + 3 / 2) < 1e-6)

    sol = solve_with_formula(3, 5, 3)
    assert(sol == [])
    sol = solve_with_formula(-2, 4, 1)
    assert(abs(sol[0] + sol[1] + 4 / -2) < 1e-6)
    assert(abs(sol[0] * sol[1] + 1 / 2) < 1e-6)

    assert(solve_with_formula(0, 0, 5) == [])
    assert(solve_with_formula(0, 5, 0) == [0])
    assert(solve_with_formula(0, 0, 0) == None)
    print("Section 2 正确")

    print("正在检查 Section 3：")
    f = lambda x: math.log(x) + x
    assert(abs(solve_equation(f) - 0.567143290) < 1e-6)
    f = lambda x: x ** 3 - 7 * x ** 2 + 11 * x + 3
    assert(
        abs(solve_equation(f) - 3) < 1e-6 or
        abs(solve_equation(f) - (2 - math.sqrt(5))) < 1e-6 or
        abs(solve_equation(f) - (2 + math.sqrt(5))) < 1e-6
        )
    f = lambda x: -3 * (x ** 3) + (x ** 2) + 9
    assert(abs(solve_equation(f) - 1.5623574989) < 1e-6)
    print("Section 3 正确")
