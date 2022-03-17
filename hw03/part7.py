# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
from random import randint

size = 30
limit = abs(10)
numbers = [randint(-limit, limit) for _ in range(size)]
print(numbers)

last = prev = None
for number in numbers:
    if last is None:
        last = number
    elif number < last:
        prev, last = last, number
    elif prev is None or number < prev:
        prev = number
print(last, prev)
