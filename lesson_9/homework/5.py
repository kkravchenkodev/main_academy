"""
Создать словарь, где ключ - значение списка users, значение - значение списка marks
users = ["Ann", "Jane", "Bob", "Bill", "John"]
marks = [5, 4, 3, 4, 5]
# result = {'Ann': 5, 'Jane': 4, 'Bob': 3, 'Bill': 4, 'John': 5}
"""

users = ["Ann", "Jane", "Bob", "Bill", "John"]
marks = [5, 4, 3, 4, 5]
print(dict(zip(users, marks)))
