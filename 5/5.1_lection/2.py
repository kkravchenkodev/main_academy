"""
2. Спросить пользователя число и напечатать список всех делителей
N = 8
result = [1, 2, 4, 8]
"""

n = int(input())
output = []
for i in range(1, n + 1):
    if n % i == 0:
        output.append(i)
print(output)