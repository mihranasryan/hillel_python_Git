#: Сделать программу в виде функций в которой нужно будет угадывать число.
import random


def guess_the_number():
    random_number = random.randint(1, 10)
    attempts_made = 1
    while attempts_made <= 3:
        entered_number = int(input('Введите целое число от 1 до 10: '))
        attempts_made += 1
        if entered_number < random_number:
            print('Введенное число меньше загадываемого.')
            continue
        if entered_number > random_number:
            print('Введенное число больше загадываемого.')
            continue
        if entered_number == random_number:
            print('Отлично! Вы угадали.')
            break
    if attempts_made > 3:
        print('You lose!')


def play_again():
    while True:
        ask_to_play = input('Сыграем еще?(Д/Y)\nЕсли нет,нажмите любую другую кнопку: ')
        if ask_to_play.upper() in ('Д', 'Y'):
            guess_the_number()
        else:
            print('До новых встреч!')
            break


guess_the_number()
play_again()
