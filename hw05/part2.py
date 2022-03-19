# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому
# использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
__hex_to_dec = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def test_sum(fun):
    assert ['C', 'F', '1'] == fun("A2", "C4F")


def test_mult(fun):
    assert ['7', 'C', '9', 'F', 'E'] == fun("A2", "C4F")


def aligning(a, b):
    dif = len(a) - len(b)
    if dif < 0:
        a = "0" * abs(dif) + a
    else:
        b = "0" * dif + b
    return a[::-1], b[::-1]


def hex_sum(a, b):
    a, b = aligning(a, b)
    result = []
    transfer = 0
    for i in range(len(a)):
        digit_a = __hex_to_dec.index(a[i])
        digit_b = __hex_to_dec.index(b[i])
        digit_result = digit_a + digit_b + transfer
        result.insert(0, __hex_to_dec[digit_result % 16])
        transfer = digit_result // 16
    if transfer > 0:
        result.insert(0, __hex_to_dec[transfer])
    return result


def hex_mult(a, b):
    a, b = aligning(a, b)
    dim_number = len(a)
    result = []
    transfer = 0
    for j in range(dim_number * 2 - 1):
        digit_result = transfer
        for i in range(dim_number):
            if i <= j < dim_number + i:
                digit_a = __hex_to_dec.index(a[j - i])
                digit_b = __hex_to_dec.index(b[i])
                digit_result = digit_result + digit_a * digit_b
        result.insert(0, __hex_to_dec[digit_result % 16])
        transfer = digit_result // 16
    if transfer > 0:
        result.insert(0, __hex_to_dec[transfer])
    return result


def input_hex(operand_name):
    while True:
        operand = input(f"Введите значение {operand_name} в 16чной системе: ").upper()
        if set(operand).issubset(set(__hex_to_dec)):
            return operand


test_sum(hex_sum)
test_mult(hex_mult)
number_a = input_hex("A")
number_b = input_hex("B")
print(f"{number_a}+{number_b}={hex_sum(number_a, number_b)}")
print(f"{number_a}+{number_b}={hex(int(number_a, 16) + int(number_b, 16))}")
print(f"{number_a}*{number_b}={hex_mult(number_a, number_b)}")
print(f"{number_a}*{number_b}={hex(int(number_a, 16) * int(number_b, 16))}")
