import random
import string

"""
object pool
data types
"""

res = 12 / 5

print(res)

max("sad")
print(max("saddfdf"))

random.seed(120)
print(random.randint(0, 100))

lst = ['1', '31', 'true', True]
random.choice(lst)

s = "abcdefghigklmnop"

random.shuffle(lst)
print(lst)

s1 = 'qwertyuiop[]qwe'
s2 = 'qwertyuiop[]'
print(s1 is s2)

# ''.replace()
# ''.isalpha()
# ''.isnumeric()
#
# ''.rjust()
# ''.ljust()
# ''.rstrip()
# ''.lstrip()
# ''.strip()

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)

# for i in string.printable:
#     print(ord(i))

var = string.printable[-1]  # whitespace
print(ord(var))
a, b = [1, 2]
print(a)
print(b)