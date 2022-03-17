# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа
# '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать
# пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
def input_operand(name, is_division=False):
    while True:
        operand = input(f"Введите целое число в качестве операнда {name}: ")
        if operand.isdigit():
            operand = int(operand)
            if is_division and operand == 0:
                print(f"Ошибка ввода операнда {name}. Попытка деления на 0.")
            else:
                return operand
        else:
            print(f"Ошибка ввода операнда {name}. Введите целое число")


def input_operation_sign():
    available_sign = ['+', '-', '*', '/', '0']
    while True:
        sign = input("Введите знак операции ('+' для сложения, '-' для вычитания, '*' для умножения, '/' "
                     "для деления) или '0' для выхода: ")
        if sign in available_sign:
            return sign
        else:
            print("Ошибка ввода знака операции.")


while True:
    operation = input_operation_sign()
    if operation == '0':
        print("Выходим...")
        break
    operand_a = input_operand("A")
    operand_b = input_operand("B", operation == '/')
    if operation == '+':
        print(f"Результат операции: {operand_a + operand_b}")
    elif operation == '-':
        print(f"Результат операции: {operand_a - operand_b}")
    elif operation == '*':
        print(f"Результат операции: {operand_a * operand_b}")
    elif operation == '/':
        print(f"Результат операции: {operand_a / operand_b}")
