# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
from random import randint

size = 20
numbers = [randint(0, 100) for _ in range(size)]
# Вариант 1
even_index = [ind for ind, x in enumerate(numbers) if x % 2 == 0]
print(numbers)
print(even_index)
# Вариант 2
even_index = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]
print(numbers)
print(even_index)
