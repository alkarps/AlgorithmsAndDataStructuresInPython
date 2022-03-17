# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.
from random import randint


def input_number():
    while True:
        number = input("Введите число от 0 до 100: ")
        if number.isdigit():
            number = int(number)
            if 0 <= number <= 100:
                return number
        print("Ошибка ввода.")


number = randint(0, 100)
for i in range(10):
    user_number = input_number()
    if number == user_number:
        print("Число угадано.")
        break
    if number > user_number:
        print(f"Загаданное число > {user_number}")
    else:
        print(f"Загаданное число < {user_number}")
else:
    print(f"Загаданное число {number}")
