# https://www.codewars.com/kata/644661194e259c035311ada7/train/python
def mul_by_n(lst, n):
    print("Inputs: ", lst, n)
    result = list(x * n for x in lst)
    print("Result: ", list(result))
    return list(result)