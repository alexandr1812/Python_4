# . Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`

def red_file():
    list_word = []
    with open('text_words.txt', encoding='utf-8') as data:
        for line in data:
            list_word.append(line.strip())
    return list_word


def write_life(list_in):
    with open('text_code_words.txt', 'w', encoding='utf-8') as data:
        for i in list_in:
            data.write(i + "\n")


def encode(s):
    encoding = ""
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding


if __name__ == '__main__':
    list_incode = []
    result = red_file()

    for i in range(0, len(result)):
        list_incode.append(encode(result[i]))
    write_life(list_incode)
