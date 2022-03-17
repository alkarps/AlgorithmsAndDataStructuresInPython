# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from random import randint

size = 100
limit = abs(100)
numbers = [randint(-limit, limit) for _ in range(size)]
print(numbers)

max_negative_number = None
for number in set(numbers):
    if number < 0 and (max_negative_number is None or number > max_negative_number):
        max_negative_number = number
print(max_negative_number)
