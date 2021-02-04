"""
Write a program that given an array of integers determines if it is sorted in "ascending" order,
"descending" order or "not sorted" at all.

Example
For a = [10, 5, 4], the output should be
order(a) = "descending";
For a = [6, 20, 160, 420], the output should be
order(a) = "ascending";
For a = [1, 7, 0, 4, 8, 1], the output should be
order(a) = "not sorted".
[input] array.integer a
1 < a.length < 100, all of numbers are different
[output] string
"ascending", "descending" or "not sorted".
"""


def order(a):
    if a == sorted(a):
        return "ascending"
    elif a == sorted(a, reverse=True):
        return "descending"
    else:
        return "not sorted"


print(order([10, 1, 5, 4]))
print(order([6, 20, 5, 160, 420]))
print(order([1, 7, 0, 4, 8, 1]))
