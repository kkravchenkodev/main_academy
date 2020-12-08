"""
Посчитать сумму каждого третьего элемента в списке
Например:
lst = [1,2,3,4,5,6,7,8]
result: 12
"""
import random

n = int(input("Enter list size: "))
lst = [random.randint(0, 10) for _ in range(n)]
print(lst)

print(sum(lst[::3]))
