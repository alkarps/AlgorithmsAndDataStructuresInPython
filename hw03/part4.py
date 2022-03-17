# Определить, какое число в массиве встречается чаще всего.
from random import randint

size = 100
numbers = [randint(0, 10) for _ in range(size)]
print(numbers)

frequent_number = -1
frequent_number_count = 0
for number in set(numbers):
    current_frequent = numbers.count(number)
    if current_frequent > frequent_number_count:
        frequent_number = number
        frequent_number_count = current_frequent
print(frequent_number, frequent_number_count)
