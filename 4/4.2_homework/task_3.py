"""
Написать программу, которая удаляет слова, короче 5 символов
input: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result: ['Red', 'Pink']
"""


def del_words(lst):
    return [e for e in lst if len(e) < 5]


inp_lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(del_words(inp_lst))
