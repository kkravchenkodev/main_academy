import os
import converter

if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__)) + '/data.txt'
    print('-' * 35)
    converter.convert_1(path)
    print('-' * 35)
    converter.convert_2(path)
    print('-' * 35)
    converter.convert_3(path)
    print('-' * 35)
    converter.convert_4(path)
