# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]


def list_of_multipliers(number):
    while number <= 0:
        print('Enter a positive value')
        number = int(input('Try again: '))


    arr = []
    divider = 2
    while number > 1:
        if number % divider == 0:
            arr.append(divider)
            res = number // divider
            number = res
        else:
            number % divider != 0
            divider += 1
    return arr

print(list_of_multipliers(int(input('Enter the number: '))))