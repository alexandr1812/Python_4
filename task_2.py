# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]


def create_list(num):
    while num <= 0:
        print('Enter a positive value')
        num = int(input('Try again: '))
    
    list_num = [i for i in range(20, num+1)]
    return list_num


def list_with_new_value(first_list: list):
    result = []
    for i in range(len(first_list)):
        if first_list[i] % 20 == 0 or first_list[i] % 21 == 0:
            result.append(first_list[i])
    return result


print(list_with_new_value(create_list(int(input('Enter a positive value from 20 or more: ')))))
