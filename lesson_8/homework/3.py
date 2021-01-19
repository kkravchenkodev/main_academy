"""
Дан дикт с инфо о студенте, вернуть только те ключ-значение, если ключ есть в personal_info
# result = {
#         "id": 1,
#         "name": "Ann",
#         "age": 18,
#         "gender": "female"
#     }
"""
import json

student = {
    "id": 1,
    "name": "Ann",
    "age": 18,
    "gender": "female",
    "score": 40
}
personal_info = ["id", "name", "age", "gender"]

res = {key: value for key, value in student.items() if key in personal_info}
print(json.dumps(res, indent=2))
