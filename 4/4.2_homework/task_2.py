"""
написать функцию, которая принимает список любых значений и возвращает список только тех значений,
которые содержат только буквы
input: ['yellow', 'red', 'one', 'two', 3, '4', 'five5"]
result: ['yellow', 'red', 'one', 'two']
"""
import string


def filter_list(lst):
    target = []
    for each in lst:
        if not isinstance(each, str):
            continue
        elif set(each) & set(string.digits):
            continue
        else:
            target.append(each)
    return target


inp_lst = ['111', 'yellow', 'red', 'one', 'two', 3, '4', 'five5']
print(inp_lst)
print(filter_list(inp_lst))
