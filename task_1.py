# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample


# num = int(input())
# result = []
# first_list = [i for i in sample(range(1, num * 2), k=num)]
# for i in range(len(first_list)-1):
#     if first_list[i] < first_list[i+1]:
#         result.append(first_list[i+1])

# print(first_list)
# print(result)


def create_list(num):
    while num <= 0:
        print('Enter a positive value')
        num = int(input('Try again: '))

    list_num = [i for i in sample(range(1, num * 2), k=num)]
    return list_num


first_list_of_numbers = create_list(int(input('Enter a positive value: ')))
print(first_list_of_numbers)


def new_value_in_list(first_list: list):
    list_result = []
    for i in range(len(first_list)-1):
        if first_list[i] < first_list[i+1]:
            list_result.append(first_list[i+1])
    return list_result


print(new_value_in_list(first_list_of_numbers))
