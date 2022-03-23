# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
from random import randint, choice
from statistics import median


def test_sort(fun):
    size = 100
    array = [randint(-100, 100) for _ in range(2 * size + 1)]
    expected = median(array)
    actual = fun(array)
    assert expected == actual, f"Найденная медиана {actual} не равна ожидаемой {expected}"


def custom_median(array, k=None):
    if k is None:
        k = len(array) / 2
    if len(array) == 1:
        assert k == 0
        return array[0]

    pivot = choice(array)

    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(lows):
        return custom_median(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return custom_median(highs, k - len(lows) - len(pivots))


if __name__ == "__main__":
    test_sort(custom_median)
