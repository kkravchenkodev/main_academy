"""
Написать программу, которая перемножит все числа в спике.
input: [1, 2, 3, 4]
result: 24
"""


def multiply(lst):
    s = 1
    for i in lst:
        s *= i
    return s


print(multiply([1, 2, 3, 4, 5, 6, 7, 8, 9]))
