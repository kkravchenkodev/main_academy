"""
3. Написать декоратор, который выводит время выполнения функции.
"""
import time


def timer(func):
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print(f'{func.__name__} method takes {te - ts:f} ms')
        return result
    return wrapper


@timer
def lucky():
    array = [1] * 10 + [0] * 28
    for i in range(2):
        array = [sum(array[x::-1]) if x < 10 else sum(array[x:x - 10:-1]) for x in range(28)]
    # print([x ** 2 for x in array])
    print(sum([x ** 2 for x in array]))


lucky()
