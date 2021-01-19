"""
создать список с именами студентов, если их ID есть в списке student_ids

# result = ['Ann', 'John', 'Bob', 'Bill']
"""
students = [
    {
        "id": 1,
        "name": "Ann"
    },
    {
        "id": 2,
        "name": "John"
    },
    {
        "id": 3,
        "name": "Bob"
    },
    {
        "id": 4,
        "name": "Bill"
    },
    {
        "id": 5,
        "name": "Jane"
    }
]
student_ids = [1, 2, 3, 4, 6, 7]
# result = [st['name'] for st in students if st['id'] in student_ids]
result = [st['name'] if st['id'] in student_ids else f"{{{st['name']}}}" for st in students]
print(result)
