"""
Вернуть список студентов, у которых бал больше 50
"""
import json

students = [
    {
        "id": 1,
        "name": "Ann",
        "score": 40
    },
    {
        "id": 2,
        "name": "John",
        "score": 50
    },
    {
        "id": 3,
        "name": "Bob",
        "score": 100
    },
    {
        "id": 4,
        "name": "Bill",
        "score": 80
    },
    {
        "id": 5,
        "name": "Jane",
        "score": 60
    }
]
threshold = 50

result = [st for st in students if st['score'] > threshold]
print(json.dumps(result, indent=2))
