# * 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

import random


def write_file(string):
    with open('filegood.txt', 'a') as data:
        data.write(string)
    with open('filegood2.txt', 'a') as data:
        data.write(string)


def rnd():
    return random.randint(0, 101)


def create_list(k):
    array = [rnd() for i in range(k+1)]
    return array


def create_str(sp):
    array = sp[::-1]
    wr = '\n'
    if len(array) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(array)):
            if i != len(array) - 1 and array[i] != 0 and i != len(array) - 2:
                wr += f'{array[i]}*x^{len(array)-i-1}'
                if array[i+1] != 0:
                    wr += ' + '
            elif i == len(array) - 2 and array[i] != 0:
                wr += f'{array[i]}*x'
                if array[i+1] != 0:
                    wr += ' + '
            elif i == len(array) - 1 and array[i] != 0:
                wr += f'{array[i]} = 0'
            elif i == len(array) - 1 and array[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Enter natural power k ="))
coefficient = create_list(k)
write_file(create_str(coefficient))
