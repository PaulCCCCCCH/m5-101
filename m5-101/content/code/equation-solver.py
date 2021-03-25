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
    ######################
    ### Your code here ###
    ######################
    return None

#################
### Section 2 ###
#################
def solve_with_formula(a, b, c):
    """
    求解方程　ax^2 + bx + c = 0
    """
    ######################
    ### Your code here ###
    ######################
    return None

#################
### Section 3 ###
#################
def solve_equation(f):
    """
    求解方程 f = 0
    """
    ######################
    ### Your code here ###
    ######################
    return None

def section1_test(case):
    args = case[0] # (a, b)
    ans = case[1]  # correct ans
    sol = solve_linear(args[0], args[1])
    res = False
    if sol == ans or (ans != None and len(ans) == 1 and sol != None and len(sol) == 1 and abs(sol[0] - ans[0]) < 1e-6):
      res = True
    print('Case ' + str(args[0]) + 'x^2+' + str(args[1]) + '=0: 正确结果为 ' + str(ans) + '，你的结果为 ' + str(sol) + '。')
    if res: 
      print('检查通过。')
    else:   
      print('检查失败。')
    assert(res == True)

def section2_test(case):
    args = case[0] # [a, b, c]
    number_of_ans = case[1]  # -1 for question with countless solutions
    sol = solve_with_formula(args[0], args[1], args[2])
    res = False
    if number_of_ans == 1 and sol != None and len(sol) == 1:
      if args[0] != 0:
        res = abs(sol[0]+sol[0] + args[1]/args[0]) < 1e-6 and abs(sol[0]*sol[0] - args[2] / args[0]) < 1e-6
      else:
        res = abs(sol[0] + args[2]/args[1]) < 1e-6
    elif number_of_ans == 2 and sol != None and len(sol) == 2:
      res = abs(sol[0]+sol[1] + args[1]/args[0]) < 1e-6 and abs(sol[0]*sol[1] - args[2] / args[0]) < 1e-6
    elif number_of_ans == 0 and sol != None and sol == []:
      res = True
    elif number_of_ans == -1 and sol == None:
      res = True
    print('Case ' + str(args[0]) + 'x^2+' + str(args[1]) + 'x+' + str(args[2]) + '=0: 你的结果为 ' + str(sol) + '。')
    if res: 
      print('结果正确。')
    else:   
      print('结果错误。')
    assert(res == True)
    
def section3_test(case):
    question_str = case[0] 
    question_f = case[1]
    ans = case[2]
    sol = solve_equation(question_f)
    res = False
    for a in ans:
      if abs(sol - a) < 1e-6:
        res = True
        break
    print('Case ' + question_str + '=0: 你的结果为 ' + str(sol) + '。')
    if res: 
      print('结果正确。')
    else:   
      print('结果错误。')
    assert(res == True)



if __name__ == "__main__":
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

