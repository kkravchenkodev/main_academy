"""
Написать генератор, который принимает параметры так же, как range.
может быть вызван так:
my_range(10) # stop
my_range(2, 10) # start, stop
my_range(2, 10, 2) # start, stop, step (edited)
"""
import sys


def my_range(*args, **kwargs):
    step, start, stop = 0, 0, 0
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    if len(args) == 2:
        start, stop, step = args[0], args[1], 1
    if len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


gnr = my_range(0, -10, -1)
print('Generator sizeof is - {}'.format(sys.getsizeof(gnr)))
lst = list(my_range(0, -10, -1))
print(lst)
print('List sizeof is - {}'.format(sys.getsizeof(lst)))
