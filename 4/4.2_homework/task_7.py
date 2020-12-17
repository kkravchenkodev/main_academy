"""
Написать программу, которая принимает 2 аргумента: список элементов любого типа и элемент любого типа.
Программа возвращает кол-во вхождений элемента в список. (аналог lst.count(n))
input: [1, 2, 3, "one", "onetwo", "one"]
result: 2
"""

input_data = [1, 2, 3, "one", "onetwo", "one", 2, 3, 4, 2, 6, 0, 1.2, 3.4, 12, 3, 1.2]


def custom_counter(lst, element):
    count = 0
    filtered_list = list(filter(lambda item: isinstance(item, type(element)), lst))
    for i in filtered_list:
        if i == element:
            count += 1
    return count


lst2 = custom_counter(input_data, 3)
print(lst2)
