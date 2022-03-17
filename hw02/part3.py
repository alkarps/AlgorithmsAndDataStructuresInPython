# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
def input_number():
    while True:
        number = input("Введите натуральное число: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
        print("Ошибка ввода.")


def arithmetic_revers(number):
    reversed_number = 0
    while number > 0:
        reversed_number *= 10
        digit = number % 10
        reversed_number += digit
        number //= 10
    return reversed_number


origin_number = input_number()
print(f"Новое число: {arithmetic_revers(origin_number)}")
