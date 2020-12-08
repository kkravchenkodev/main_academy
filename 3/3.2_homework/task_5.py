"""
Написать программу несколькими способами, которая удаляет n-й символ из непустой строки.
s = “environment”
n = 3
result: envronment
"""
s = 'environment'
n = 3
print(s)

# way 1
print(s.replace(s[n], ''))

# way 2
lst = [*s]
del lst[n]
print(''.join(lst))

# way 3
print(s[:s.index(s[n])] + s[s.index(s[n]) + 1:])

# way 4
print("".join([x for x in s if x is not s[n]]))
