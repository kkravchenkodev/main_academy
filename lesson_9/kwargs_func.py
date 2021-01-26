from math import factorial


def multiplier(*args):
    acc = 1
    for i in args:
        acc *= i
    return acc


print(multiplier(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
print(multiplier())

# -------------------------------------------
print([i * i for i in range(9)])
print(list(map(lambda x: x * x, range(9))))

# -------------------------------------------
print([i for i in range(11) if not i % 2])
print(list(filter(lambda x: x % 2 == 0, range(11))))
