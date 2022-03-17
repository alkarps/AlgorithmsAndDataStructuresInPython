# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def input_number():
    while True:
        number = input("Введите натуральное число: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
        print("Ошибка ввода.")


def cal_even_and_odd_digit(number):
    odd = even = 0
    while number != 0:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    return odd, even


origin_number = input_number()
odd, even = cal_even_and_odd_digit(origin_number)
print(f"В введенном числе {origin_number} {odd} нечетных цифры и {even} четных цифр.")
