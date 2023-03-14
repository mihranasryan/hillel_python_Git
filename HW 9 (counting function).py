#Дан список чисел. Посчитать сколько раз в нём встречается каждое число.
#Использовать для подсчёта функцию.
#Подсказка: для хранения данных использовать словарь (ключ - само число,
#а значение - сколько раз оно встречается). Для проверки нахождения
#элемента в словаре использовать метод get(), либо оператор in.

my_list_of_number = [1, 3, 5, 6, 7, 7, 3, 4, 1, 3, 9, 8, 99, 9]


def dict_of_numbers(list_of_number):
    result = {}
    for i in list_of_number:
        if result.get(i):
            result[i] += 1
        else:
            result[i] = 1
    return result


print(dict_of_numbers(my_list_of_number))
