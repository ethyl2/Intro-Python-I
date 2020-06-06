"""
from https://www.geeksforgeeks.org/eval-in-python/
"""


def function_creator():
    expr = input("Enter a function (in terms of x): ")
    x = int(input("Enter your value for x: "))
    y = eval(expr)
    print("y = {}".format(y))


function_creator()

y = "7"
y_evaluated = eval(y)
print(type(y_evaluated))
x = 5
print(x + y_evaluated)
