# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

size = 30
limit = abs(10)
numbers = [randint(-limit, limit) for _ in range(size)]
print(numbers)

start = end = 0
for i in range(len(numbers)):
    if numbers[i] < numbers[start]:
        start = i
    if numbers[i] > numbers[end]:
        end = i
if start > end:
    end, start = start, end
sum_number = 0
for i in range(start + 1, end):
    sum_number += numbers[i]
print(numbers[start + 1:end])
print(sum_number)
