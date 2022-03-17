# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
def input_number():
    while True:
        number = input("Введите натуральное число: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
        print("Ошибка ввода.")


def check_equals(n):
    left_equals = 0
    for i in range(1, n + 1):
        left_equals += i
    right_equals = n * (n + 1) / 2
    return left_equals == right_equals


n = input_number()
for i in range(1, n):
    if not check_equals(i):
        print(f"Равенство не выполняется для числа {i}!")
        break
else:
    print(f"Равенство выполняется для множества чисел от 0 до {n}!")
