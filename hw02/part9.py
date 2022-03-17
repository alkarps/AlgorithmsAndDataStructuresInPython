# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def input_number():
    while True:
        number = input("Введите натуральное число: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
        print("Ошибка ввода.")


def sum_number_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum


max_number = max_sum_number = 0
while True:
    current_number = input_number()
    current_sum_number = sum_number_digits(current_number)
    if current_sum_number > max_sum_number:
        max_number, max_sum_number = current_number, current_sum_number
    if input("Для продолжения ввода нажмите на ENTER или введите что-нибудь для остановки: ") != "":
        break
print(f"Среди введенных чисел максимальная сумма цифр равная {max_sum_number} у числа {max_number}")
