"""
Input data (part1.txt)
——————————————————
Login;Name;Email
ivanov;Ivan Ivanov;ivanov@mail.com
петров;Петр Петров;petrov@google.com
obama;Barack Obama;obama@google.com
bush;Джордж Буш;bush@mail.com
——————————————————
Необходимо написать 4 функции-конвертера, результатом работы которых будут следующие выводы:


Output of convert1
——————————————————
ivanov: ivanov@mail.com
петров: petrov@google.com
obama: obama@google.com
bush: bush@mail.com
——————————————————
Output of convert2
——————————————————
Ivanov Ivan (email: ivanov@mail.com)
Петров Петр (email: petrov@google.com)
Obama Barack (email: obama@google.com)
Буш Джордж (email: bush@mail.com)
——————————————————
Output of convert3
——————————————————
mail.com ==> ivanov, bush
google.com ==> петров, obama
——————————————————
Output of convert4
It should convert input data to a string of the following type (Password column should be added,
the password itself should contain exactly 4 digits that are generated randomly):
——————————————————
Login;Name;Email;Password
ivanov;Ivan Ivanov;ivanov@mail.com;1707
петров;Петр Петров;petrov@google.com;9321
obama;Barack Obama;obama@google.com;4623
bush;Джордж Буш;bush@mail.com;7514
"""