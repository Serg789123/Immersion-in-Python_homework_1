# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше”
# или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
search_num = randint(LOWER_LIMIT, UPPER_LIMIT)
num = -1
count = 0

while search_num != num:
    num = int(input(f"Введите среднеарифметическое (округлённое до целого), между {LOWER_LIMIT} и {UPPER_LIMIT}: "))
    count += 1
    if search_num == num:
        print(f"Вы угадали число за количество попыток = {count}")
        break
    elif num < search_num:
        LOWER_LIMIT = num
        print("Загаданное число больше")
    elif num > search_num:
        UPPER_LIMIT = num
        print("Загаданное число меньше")
