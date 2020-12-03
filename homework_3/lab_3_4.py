#!/usr/bin/env python3

"""
Additional_practice_work_1
# Generate string with lowercase and uppercase alphabet plus numbers
# Print 1st symbol of string
# Print last symbol
# Print 3rd from start and 3rd from the end
# Slice first 8 symbols
# Print only symbols with index, which divides on 3 without remaining
# Print the symbol of the middle of the string text
# Reverse text using slice
"""
import random
import string


def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for _ in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


generated_string = get_random_string(30)
print(generated_string[0])
print(generated_string[-1])
print(generated_string[2], generated_string[-3], sep=' ')
print(generated_string[:8])
print(generated_string[::3])
print(generated_string[len(generated_string) // 2])
print(generated_string[::-1])
