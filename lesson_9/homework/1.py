"""
Написать программу, которая создает список, содержащий длину каждого слова, длиннее чем переменная n
использовать list comprehension
n = 2
sentence = "Python is a programming language that lets you work quickly and integrate systems more effectively."
"""

sentence = "Python is a programming language that lets you work quickly and integrate systems more effectively."
n = int(input('Enter word length to filter: '))
print([i for i in sentence.split() if len(i) > n])
