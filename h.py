#  Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

from random import choices


def word_generation(count_word):
    while count_word <= 0:
        print('incorrect value')
        count_word = int(input('Try again: '))

    word = []
    for i in range(count_word):
        symbols = choices('абв', k=3)
        word.append(''.join(symbols))
        string_conversion = ' '.join(map(str, word))
    return string_conversion


def delete_word(list_word):
    stop_word = 'абв'
    parsing_list = list_word.split()
    word_processing = ' '.join(
        filter(lambda i: i not in stop_word, parsing_list))
    return word_processing


word_list = word_generation(int(input('Enter a positive value: ')))
print(word_list)
print(delete_word(word_list))
