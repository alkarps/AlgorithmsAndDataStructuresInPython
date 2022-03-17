# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
multiples = [0] * 8
for number in range(2, 100):
    for i in range(8):
        if number % (i + 2) == 0:
            multiples[i] += 1

for ind, multiple in enumerate(multiples):
    print(f"Кратных {ind + 2} - {multiple}")
