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


def word_generator(count_word):
    while count_word <= 0:
        print('Enter a positive value')
        count_word = int(input('Try again: '))

    words = []
    for i in range(count_word):
        symbol = choices('абв', k=3)
        words.append("".join(symbol))
        conversion_string = ' '.join((map(str, words)))
    return conversion_string


def word_deletion(word_list):
    stop_words = 'абв'
    parsing = word_list.split()
    result = ' '.join(filter(lambda i: i not in stop_words, parsing))
    return result


result = word_generator(int(input()))
print(result)
print(word_deletion(result))
