# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

employee_list = ["Иван", "Мария", "Петр", "Илья",
            "Марина", "Петр", "Алина", "Бибочка"]

def neme_sorter(name_list: list):
    newList = sorted(name_list)
    dictionary = {}
    for name in newList:
        name.capitalize()
        simbol = name[0]
        dictionary[simbol] = dictionary.setdefault(
            simbol, []) + [name.capitalize()]
    return dictionary


print(employee_list)
print(neme_sorter(employee_list))