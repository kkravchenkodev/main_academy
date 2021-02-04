"""
4. Написать логгер, который записывает в файл, какая функция и сколько выполнялась.
логгер - это декоратор, который принимает параметром имя файла.
"""


def logging(func):
    from time import ctime, time

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log_file.log', 'a') as f:
            f.write(f'function name {func.__name__} with result = {result}. Start at {ctime(time())}\n')
        # print(f'function name {func.__name__} with result = {result}. Start at {ctime(time())}\n')
        return result

    return wrapper


@logging
def my_sum(*args):
    return sum([i for i in args])


print(my_sum(5, 7, 9))
print(my_sum(*list(range(12))))
print(my_sum(*list(range(55))))
print(my_sum(*list(range(0))))
print(my_sum(*list(range(0, 100, 2))))
