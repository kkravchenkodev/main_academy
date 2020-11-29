matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix_transposed = list(map(list, zip(*matrix)))

print(matrix)
print(matrix_transposed)

# Функция zip позволяет пройтись одновременно по нескольким итерируемым объектам (спискам и др.)
# Выражение zip(a, b) создает объект-итератор, из которого при каждом обороте цикла извлекается кортеж,
# состоящий из двух элементов. Первый берется из списка a, второй - из b.
values = [1.34, 3.25, 2.99]
coefficient = [3, 2, 2]
for i, j in zip(values, coefficient):
    print(i * j)

a = []
b = []
for i, j in zip(range(10, 20), range(1, 10)):
    a.append(i)
    b.append(j)
print(a)
print(b)
