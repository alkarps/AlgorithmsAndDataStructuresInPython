# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
# комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после
# каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.
#
# Для работы требуется установить модуль profilehooks (pip install profilehooks) и
# memory_profiler (pip install -U memory_profiler)
from memory_profiler import profile as memprof
from profilehooks import profile as cprof


@memprof
# @cprof(immediate=True)
def sum_series_while(n):
    """
    Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Для вычисления используется цикл и прямое вычисление следующего числа в ряду. Сложность O(n*log(n)).
    :param n: количество элементов, для которых нужно посчитать сумму.
    :return: сумма
    """
    sum_values = 0
    while n > 0:
        sum_values += (-0.5) ** (n - 1)
        n -= 1
    return sum_values


# cprof: 2 function calls in 0.929 seconds
#
#    Ordered by: cumulative time, internal time, call count
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.929    0.929    0.929    0.929 part1.py:21(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         0    0.000             0.000          profile:0(profiler)
#
# memprof:
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     20     16.5 MiB     16.5 MiB           1   @memprof
#     21                                         # @cprof(immediate=True)
#     22                                         def sum_series_while(n):
#     23                                             """
#     24                                             Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#     25                                             Для вычисления используется цикл и прямое вычисление следующего числа в ряду. Сложность O(n*log(n)).
#     26                                             :param n: количество элементов, для которых нужно посчитать сумму.
#     27                                             :return: сумма
#     28                                             """
#     29     16.5 MiB      0.0 MiB           1       sum_values = 0
#     30     16.5 MiB      0.0 MiB     1000001       while n > 0:
#     31     16.5 MiB      0.0 MiB     1000000           sum_values += (-0.5) ** (n - 1)
#     32     16.5 MiB      0.0 MiB     1000000           n -= 1
#     33     16.5 MiB      0.0 MiB           1       return sum_values

@memprof
# @cprof(immediate=True)
def sum_series_for_with_iterator(n):
    """
    Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Для вычисления используется цикл и вычисление следующего числа в ряду на основе предыдущего. Сложность O(n).
    :param n: количество элементов, для которых нужно посчитать сумму.
    :return: сумма
    """
    sum_values = current_value = 1.0
    for i in range(n - 1):
        current_value /= -2
        sum_values += current_value
    return sum_values


# cprof: 2 function calls in 0.189 seconds
#
#    Ordered by: cumulative time, internal time, call count
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.189    0.189    0.189    0.189 part1.py:37(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         0    0.000             0.000          profile:0(profiler)
#
# memprof:
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     43     16.4 MiB     16.4 MiB           1   @memprof
#     44                                         # @cprof(immediate=True)
#     45                                         def sum_series_for_with_iterator(n):
#     46                                             """
#     47                                             Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#     48                                             Для вычисления используется цикл и вычисление следующего числа в ряду на основе предыдущего. Сложность O(n).
#     49                                             :param n: количество элементов, для которых нужно посчитать сумму.
#     50                                             :return: сумма
#     51                                             """
#     52     16.4 MiB      0.0 MiB           1       sum_values = current_value = 1.0
#     53     16.4 MiB      0.0 MiB     1000000       for i in range(n - 1):
#     54     16.4 MiB      0.0 MiB      999999           current_value /= -2
#     55     16.4 MiB      0.0 MiB      999999           sum_values += current_value
#     56     16.4 MiB      0.0 MiB           1       return sum_values

@memprof
# @cprof(immediate=True)
def sum_series_form(n):
    """
    Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Для вычисления используется формула вычисления суммы геометрической прогрессии. Сложность O(1).
    :param n: количество элементов, для которых нужно посчитать сумму.
    :return: сумма
    """
    return ((-0.5) ** n - 1) / -1.5


# cprof: 2 function calls in 0.000 seconds
#
#    Ordered by: cumulative time, internal time, call count
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 part1.py:53(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         0    0.000             0.000          profile:0(profiler)
#
# memprof:
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#    102     16.4 MiB     16.4 MiB           1   @memprof
#    103                                         # @cprof(immediate=True)
#    104                                         def sum_series_form(n):
#    105                                             """
#    106                                             Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#    107                                             Для вычисления используется формула вычисления суммы геометрической прогрессии. Сложность O(1).
#    108                                             :param n: количество элементов, для которых нужно посчитать сумму.
#    109                                             :return: сумма
#    110                                             """
#    111     16.4 MiB      0.0 MiB           1       return ((-0.5) ** n - 1) / -1.5
#
# Из данных и кода, указанных выше видно, что:
# 1. При реализации функции sum_series_while мы тратим время на возведение в степень для вычисления каждого элемента.
#   Так же мы выделяем память для вычисления следующего элемента последовательности и перезаписывании n и sum_values.
#   Не смотря на то, что значение следующего элемента, n и sum_values - промежуточные данные, потребление памяти
#   составляет O(n).
# 2. При реализации функции sum_series_for_with_iterator мы тратим время на вычисление следующего элемента относительно
#   предыдущего, тем самым уменьшая время вчисления следующего элемента, а следовательно и сложность алгоритма.
#   Тем не менее мы так же вынуждены выделять память для следующего элемента, а так же тратим память на счетчик i и
#   изменение значения sum_values. Отсюда, потребление памяти O(n).
# 3. При реализации функции sum_series_form мы не тратим на вычисление элементов последовательности, а следовательно
#   нам не приходится выделять память на временные данные. Поэтому потребление памяти для данного алгоритма - O(1).
#
# Вывод: Как видно из описания выше, самый оптимальный по сложности и памяти является 3й алгоритм, тк нам не приходится
# вычислять каждый элемент последовательности.

if __name__ == "__main__":
    n = 1000000
    sum_series_for_with_iterator(n)
    sum_series_while(n)
    sum_series_form(n)
