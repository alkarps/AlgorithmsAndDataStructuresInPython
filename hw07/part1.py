# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
from random import randint


def test_sort(fun):
    size = 100
    array = [randint(-100, 100) for _ in range(size)]
    actual = fun(array)
    assert len(actual) == size
    for i in range(size - 1):
        assert actual[i] <= actual[i + 1], f"Полученный массив не отсортирован по возрастанию: " \
                                           f"{i}'й элемент {actual[i]} > {i + 1}'го элемента {actual[i + 1]}. " \
                                           f"Проверяемый массив: {actual}"
    actual = fun(array, True)
    assert len(actual) == size
    for i in range(size - 1):
        assert actual[i] >= actual[i + 1], f"Полученный массив не отсортирован по возрастанию: " \
                                           f"{i}'й элемент {actual[i]} < {i + 1}'го элемента {actual[i + 1]}. " \
                                           f"Проверяемый массив: {actual}"


def bubble_sort(income_array, desc=False):
    result = income_array[:]
    for j in range(1, len(result) - 1):
        already_sorted = True
        for i in range(len(result) - j):
            if not desc and result[i] > result[i + 1] or desc and result[i] < result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                already_sorted = False
        if already_sorted:
            break
    return result


if __name__ == "__main__":
    test_sort(bubble_sort)
