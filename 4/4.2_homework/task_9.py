"""
Написать функцию, которая печатает елку.
В самой обычной “комплектации” функция принимает значение - высоту елки.
input: 10
result:
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
"""


def print_spruce():
    for i in range(1, 11):
        print(' ' * (10 - i), '* ' * i)


def print_triangle():
    for i in range(1, 11):
        print('* ' * i)


def print_reverse_triangle():
    for i in range(1, 11):
        print('* ' * (10 - i))


print_spruce()
print_triangle()
print_reverse_triangle()
