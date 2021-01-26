"""
C помощью list comprehension сгенерировать новый список только с позитивными целыми числами
"""

numbers = [2, -2.4, 3.3, -1, 7, 12, -11, 9.5]
print([i for i in numbers if isinstance(i, int) and i >= 0])
