"""
Написать программу для подсчета суммы чисел в списке (аналог `sum([1, 2, 3])`) не использую sum, конечно.
"""
import unittest


def summary(*args):
    s = 0
    for lst in args:
        for each in lst:
            s += each
    return s


class TestSummary(unittest.TestCase):

    def test_summary(self):
        lst1 = [i for i in range(10)]
        lst2 = [i for i in range(1, 11)]
        lst3 = [i for i in range(10, 21)]

        assert summary() == 0
        assert summary(lst1) == 45
        assert summary(lst1, lst2) == 100
        assert summary(lst1, lst2, lst3) == 265


lst1 = [i for i in range(10)]
lst2 = [i for i in range(1, 11)]
lst3 = [i for i in range(10, 21)]

print(summary(lst1))  # 45
print(summary(lst2))  # 55
print(summary(lst3))  # 220

print(summary(lst2, lst3))  # 100
print(summary(lst1, lst2, lst3))  # 265


if __name__ == '__main__':
    unittest.main()
