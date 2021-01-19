"""
1. Есть 2 списка с числами. Написать метод пересечения списков
   a = [1, 2, 3, 4, 1, 2, 3]
   b = [2, 3, 4, 5, 6]
   result = [2, 3, 4]
"""

a = [1, 2, 3, 4, 1, 2, 3]
b = [2, 3, 4, 5, 6]


def intersect(lst_a, lst_b):
    target = []
    for i in lst_a:
        for j in lst_b:
            if i == j and i not in target:
                target.append(i)
    return target


print(intersect(a, b))
