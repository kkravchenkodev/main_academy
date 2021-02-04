"""
2. Написать свой декоратор, который выбирает рандомное приветствие для введенного имени
'Hello, <Name>', 'Welcome, <Name>','Greetings, <Name>!','Salutations, <Name>!','Good day, <Name>!', 'Yo, <Name>!'
"""
from random import choice

phrases = ['Hello', 'Welcome', 'Greetings', 'Salutations', 'Good day', 'Yo']


def greetings(phrase):
    def greet_wrapper(func):
        def wrapper(*args, **kwargs):
            return f'{phrase}, {func(*args, **kwargs)}'

        return wrapper

    return greet_wrapper


@greetings(choice(phrases))
def say_hello(name):
    return name


print(say_hello("Very Long Name and Surname"))
