# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
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


def merge_sort(income_array, desc=False):
    if len(income_array) < 2:
        return income_array[:]
    middle = len(income_array) // 2
    left = merge_sort(income_array[:middle], desc)
    right = merge_sort(income_array[middle:], desc)
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if not desc and left[i] < right[j] or desc and left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == "__main__":
    test_sort(merge_sort)
