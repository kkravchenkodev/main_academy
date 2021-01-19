"""
Система тестирования для студентов.
===> LEVEL 1. <===
Написать программу, которая показывает студенту 1 вопрос и 3 варианта ответов.
Просит пользователя ввести ответ (только 1 вариант верный)
Пользователь вводит 1, 2 или 3 и программа говорит - правильно или нет.
"""

correct_answer = 1

while 1:
    print('The Question is .....')
    print('1. One')
    print('2. Two')
    print('3. Three')
    print('Enter 1,2,3 for answer or 0 to exit: ')
    answer = int(input())
    if not answer:
        print('Exit...')
        break
    elif answer == correct_answer:
        print('Hooray!!! Correct answer...')
        break
    else:
        print('Try again :)')
