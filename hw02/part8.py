# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
def input_number(digit=False):
    message = "Введите натуральное число: "
    if digit:
        message = "Введите цифру от 0 до 9: "
    while True:
        number = input(message)
        if number.isdigit():
            number = int(number)
            if digit and 10 > number >= 0 or number > 0:
                return number
        print("Ошибка ввода.")


def count_digit_in_number(number, digit):
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count


digit_number = input_number(digit=True)
count_digit = 0
continue_input = True
print("Запускаем ввод последовательности...")
while continue_input:
    new_number = input_number()
    count_digit += count_digit_in_number(new_number, digit_number)
    continue_input = input("Для продолжения ввода нажмите на ENTER или введите что-нибудь для остановки: ") == ""
print(f"Количество {digit_number} в введеной последовательности равно {count_digit}")
