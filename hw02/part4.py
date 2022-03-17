# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
def sum_number_series(n):
    sum_values = current_value = 1.0
    for i in range(n - 1):
        current_value /= -2
        sum_values += current_value
    return sum_values


def sum_number_series_while(n):
    sum_values = 0
    while n > 0:
        sum_values += (-0.5) ** (n - 1)
        n -= 1
    return sum_values


def sum_number_series_form(n):
    return ((-0.5) ** n - 1) / -1.5


def input_number():
    while True:
        number = input("Введите натуральное число: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
        print("Ошибка ввода.")


n = input_number()
print(sum_number_series(n))
print(sum_number_series_while(n))
print(sum_number_series_form(n))
