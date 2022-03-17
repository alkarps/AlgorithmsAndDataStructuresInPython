# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
# в том числе написанных самостоятельно.
from random import randint

row_size = 5
column_size = 5
limit = abs(10)
matrix = [[randint(-limit, limit) for _ in range(row_size)] for _ in range(column_size)]

print("Матрица: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]:>6}", end="")
    print()

max_elem = None
max_elem_position = ()
for i in range(len(matrix)):
    min_elem = None
    min_elem_position = ()
    for j in range(len(matrix[i])):
        if min_elem is None or min_elem > matrix[j][i]:
            min_elem = matrix[j][i]
            min_elem_position = (j + 1, i + 1)
    if max_elem is None or max_elem < min_elem:
        max_elem = min_elem
        max_elem_position = min_elem_position

print(f"Максимальное число из минимальных чисел в столбцах: {max_elem} в ячейке {max_elem_position}")
