#!/usr/bin/env python3

import random
import string
import re

"""
print first symbol of list
print the last symbol of list
print 3rd from beginning and 3rd from the end symbols
make slice of first 10 symbols
print only symbols with index, which divides on 3 without
remaining
print only integer values from list
reverse integer list using slice
convert list into string with “-” separator
"""


def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for _ in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


rand_string = get_random_string(30)
gen_list = list(rand_string)
print(gen_list[0])
print(gen_list[-1])
print(gen_list[2], gen_list[-3], sep=' ')
print(gen_list[:10])
print(gen_list[::2])
print(*[int(num) for num in filter(lambda num: num.isnumeric(), gen_list)])
print(*[int(num) for num in re.findall(r'\d+', rand_string)])
print(gen_list[::-1])
print('-'.join(gen_list))
