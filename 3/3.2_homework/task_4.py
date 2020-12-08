"""
Заменить все появления 1й буквы в слове на “_”
s = “environment”
result: _nvironm_nt
"""

s = 'environment'

replaced = s.replace(s[0], '_', s.count(s[0]))
print(s)
print(replaced)
