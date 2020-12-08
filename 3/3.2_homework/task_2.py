"""
Пользователь вводит список. Найти среднее арифметическое списка
Например: lst = [10, 20, 30, 40, 55]
Результат: 31.0
"""

n = int(input("Enter a number of list items: "))
lst = [int(input()) for i in range(n)]
print(f'Среднее арифметическое списка равно {sum(lst) / len(lst):.2f}')
