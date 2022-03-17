# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
def input_number(row_index, column_index):
    while True:
        number = input(f"Введите число для ячейки {row_index + 1}:{column_index + 1} ")
        if number.isdigit():
            return int(number)
        print("Ошибка ввода.")


matrix = []
for i in range(5):
    row_sum = 0
    row = []
    for j in range(4):
        element = input_number(i, j)
        row_sum += element
        row.append(element)
    row.append(row_sum)
    matrix.append(row)

for i in range(5):
    for j in range(5):
        print(f"{matrix[i][j]:>6}", end="")
    print()
