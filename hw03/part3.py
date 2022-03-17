# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

size = 20
numbers = [randint(0, 100) for _ in range(size)]
print(numbers)

min_ind = max_ind = 0
for i in range(len(numbers)):
    if numbers[i] < numbers[min_ind]:
        min_ind = i
    if numbers[i] > numbers[max_ind]:
        max_ind = i
numbers[min_ind], numbers[max_ind] = numbers[max_ind], numbers[min_ind]
print(numbers)
