# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import choices


def create_arr(n):
    while n <= 0:
        print('Enter a positive value')
        n = int(input('Try again: '))
    arr_num = choices(range(n), k=n)
    return arr_num


generate_list = create_arr(int(input('Enter the number: ')))
print(generate_list)


def find_unique_elements(new_list):
    new_list = [a for a in new_list if new_list.count(a) == 1]
    return new_list


print(find_unique_elements(generate_list))

