"""
Написать функцию, которая принимает все 6ти значные числа.
Найти кол-во счастливых билетов (сумма первых 3х равно сумме последних 3х)
"""
import time


def timeit(method):
    def timed():
        ts = time.time()
        method()
        te = time.time()
        print(f'{method.__name__} method takes {te - ts:f} ms')

    return timed


@timeit
def lucky():
    array = [1] * 10 + [0] * 28
    for i in range(2):
        array = [sum(array[x::-1]) if x < 10 else sum(array[x:x - 10:-1]) for x in range(28)]
    # print([x ** 2 for x in array])
    print(sum([x ** 2 for x in array]))


@timeit
def lucky_with_for():
    s = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            if a + b + c == d + e + f:
                                s += 1
    print(s)


lucky()
lucky_with_for()
