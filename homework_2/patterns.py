item = '*'

print(*['\n'.join(item * i for i in range(11))])
print('\n--------------------------------------\n')

a = '*'
b = ' '

# result = ['\n'.join(a * 5 for i in range(6))]
result = (((a * 5 + b * 5) * 5 + '\n') * 3 + ((b * 5 + a * 5) * 5 + '\n') * 3) * 3
print(result)
print('\n--------------------------------------\n')
