"""
Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.
Входная строка может содержать содержит цифры, пробелы и латинские буквы.
Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.
Input -> Output:
abc12cd34ef35 -> 3
yrey424u3iou2315 -> 2 3 4
qwerty123 -> NO
"""

# 1
phrase = [i for i in input() if i.isdigit()]
phrase = sorted(set([i for i in phrase if phrase.count(i) > 1]))
print(*phrase + ['NO'][len(phrase):])

# OR 2
phrase = [i for i in input()]
phrase = sorted(set(filter(lambda x: x.isdigit() and phrase.count(x) > 1, phrase)))
print(*phrase + ['NO'][len(phrase):])

# OR 3
phrase = input()
count = {}
for ch in phrase:
    count[ch] = count.get(ch, 0) + 1
res = {k: v for k, v in count.items() if k.isdigit() and v > 1}
print(*sorted(res)) if len(res) > 0 else print('NO')
