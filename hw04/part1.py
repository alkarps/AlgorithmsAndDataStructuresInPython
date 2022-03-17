# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N
# вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)

# ВНИМАНИЕ! Приведено 2 варианта решения данного пункта. Общий вывод написан в самом конце.
def fib_rec(n):
    """
    Рекурсивный метод вычисления чисел фибоначчи. Сложность O(2^n).

    :param n: номер вычисляемого числа фибоначчи
    :return: n-е число фибоначчи
    """
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# fib_rec(5): 1000 loops, best of 5: 2.27 usec per loop
# 18 function calls (4 primitive calls) in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      15/1    0.000    0.000    0.000    0.000 part1.py:7(fib_rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_rec(10): 1000 loops, best of 5: 24.4 usec per loop
# 180 function calls (4 primitive calls) in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     177/1    0.000    0.000    0.000    0.000 part1.py:7(fib_rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_rec(15: 1000 loops, best of 5: 314 usec per loop
# 1976 function calls (4 primitive calls) in 0.001 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1973/1    0.001    0.000    0.001    0.001 part1.py:7(fib_rec)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_rec(20): 1000 loops, best of 5: 4.1 msec per loop
# 21894 function calls (4 primitive calls) in 0.010 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#   21891/1    0.010    0.000    0.010    0.010 part1.py:7(fib_rec)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_rec(25): 1000 loops, best of 5: 41.8 msec per loop
# 242788 function calls (4 primitive calls) in 0.135 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.135    0.135 <string>:1(<module>)
#  242785/1    0.135    0.000    0.135    0.135 part1.py:7(fib_rec)
#         1    0.000    0.000    0.135    0.135 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Мы можем наблюдать экспоненциальный рост сложности вычисления чисел фибоначчи.
# Так же мы видим, что повышенное использование стека вызовов.
# Все это показывает неэффективность данного подхода для решения проблемы вычисления чисел фибоначчи

def fib(n):
    """
    Метод вычисления чисел фибоначчи с помощью динамического программирования. Сложность O(n).

    :param n: номер вычисляемого числа фибоначчи
    :return: n-е число фибоначчи
    """
    if n < 2:
        return n
    fib_current, fib_prev = 1, 0
    for i in range(n - 1):
        fib_current, fib_prev = fib_current + fib_prev, fib_current
    return fib_current


# fib(5): 1000 loops, best of 5: 733 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(10): 1000 loops, best of 5: 1 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(15): 1000 loops, best of 5: 1.31 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(20): 1000 loops, best of 5: 1.66 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(25): 1000 loops, best of 5: 2.04 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(50): 1000 loops, best of 5: 4.21 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(100): 1000 loops, best of 5: 9.33 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(500): 1000 loops, best of 5: 81.5 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib(1000): 1000 loops, best of 5: 253 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:55(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Мы видим, что с помощью динамического программирования можно уменьшить время вычисления n-го числа фибоначчи,
# а так же решить проблему экспоненциального роста времени вычисления при большим n.

def fib_bin(n):
    """
    Метод вычисления чисел фибоначчи с помощью формулы Бине. Сложность O(log(n)).

    https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%91%D0%B8%D0%BD%D0%B5

    :param n: номер вычисляемого числа фибоначчи
    :return: n-е число фибоначчи
    """
    golden_ratio = (1 + 5 ** (1 / 2)) / 2
    return int((golden_ratio ** n - (-golden_ratio) ** -n) / (2 * golden_ratio - 1))


# fib_bin(5): 1000 loops, best of 5: 678 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(10): 1000 loops, best of 5: 697 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(15): 1000 loops, best of 5: 747 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(20): 1000 loops, best of 5: 739 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(25): 1000 loops, best of 5: 709 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(50): 1000 loops, best of 5: 834 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(100): 1000 loops, best of 5: 907 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(500): 1000 loops, best of 5: 1.12 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# fib_bin(1000): 1000 loops, best of 5: 1.37 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:136(fib_bin)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Мы видим, что с помощью формулы Бине можно еще уменьшить время вычисления n-го числа фибоначчи,
# а так же убрать влияние цикла на вычисление числа.

def test_sum_series(func):
    lst = [1, 0.5, 0.75, 0.625, 0.6875]
    for i, item in enumerate(lst):
        assert item == func(i + 1)


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


# sum_series_while(5): 1000 loops, best of 5: 1.89 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:275(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_while(10): 1000 loops, best of 5: 3.68 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:275(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_while(50): 1000 loops, best of 5: 18.4 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:275(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_while(100): 1000 loops, best of 5: 37.3 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:275(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_while(500): 1000 loops, best of 5: 203 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:275(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_while(1000): 1000 loops, best of 5: 424 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:275(sum_series_while)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Мы можем наблюдать, линейно-логарифмический рост времени расчета суммы n элементов ряда.
# Это связано с тем, что мы в цикле возводим в степень.
# В качестве оптимизации попробуем реализовать вычисление суммы с помощью методов динамического программирования


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


# sum_series_for_with_iterator(5): 1000 loops, best of 5: 864 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:219(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_for_with_iterator(10): 1000 loops, best of 5: 1.31 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:219(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_for_with_iterator(50): 1000 loops, best of 5: 4.82 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:219(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_for_with_iterator(100): 1000 loops, best of 5: 11.1 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:219(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_for_with_iterator(500): 1000 loops, best of 5: 49.4 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:219(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_for_with_iterator(1000): 1000 loops, best of 5: 104 usec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:219(sum_series_for_with_iterator)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Использовав метод динамического программирования мы смогли уменьшить время вычисления суммы n элементов ряда.
# Это связано с тем, что мы смогли избавиться от необходимости возводить в степень, вносящую дополнительную сложность.
# Теперь попробуем избавиться от цикла, вспомнив формулу вычисления суммы геометрической прогрессии

def sum_series_form(n):
    """
    Метод вычисления суммы n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Для вычисления используется формула вычисления суммы геометрической прогрессии. Сложность O(1).
    :param n: количество элементов, для которых нужно посчитать сумму.
    :return: сумма
    """
    return ((-0.5) ** n - 1) / -1.5


# sum_series_form(5): 1000 loops, best of 5: 356 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:331(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_form(10): 1000 loops, best of 5: 356 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:331(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_form(50): 1000 loops, best of 5: 359 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:331(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_form(100): 1000 loops, best of 5: 355 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:331(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_form(500): 1000 loops, best of 5: 346 nsec per loop
# 4 function calls in 0.000 seconds:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:331(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# sum_series_form(1000): 1000 loops, best of 5: 368 nsec per loop
# 4 function calls in 0.000 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 part1.py:331(sum_series_form)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Применив формулу вычисления суммы геометрической прогрессии мы смогли свести время вычисления суммы к константе,
# благодаря чему при большом n смогли уменьшить время вычисления на порядки
#
# ВЫВОД: исходя из выше перечисленного видно, что расчет чисел фибоначчи через формулу Бине быстрее и оптимальнее,
# чем с помощью рекурсии и метода динамического программирования. Это связано с тем, что нет необходимости вычислять
# предыдущие числа из последовательности. Для вычисления суммы n чисел из ряда 1, -0.5, 0.25, -0.125,…
# использование формулы вычисления суммы геометрической последовательности позволяет привести вычисление суммы
# к константному времени, что в значительной степени быстрее прямого вычисления каждого элемента последовательности.

if __name__ == "__main__":
    test_fib(fib_rec)
    test_fib(fib)
    test_fib(fib_bin)
    test_sum_series(sum_series_for_with_iterator)
    test_sum_series(sum_series_while)
    test_sum_series(sum_series_form)

    # cProfile.run("fib_rec(5)")
    # cProfile.run("fib_rec(10)")
    # cProfile.run("fib_rec(15)")
    # cProfile.run("fib_rec(20)")
    # cProfile.run("fib_rec(25)")
    # cProfile.run("fib(5)")
    # cProfile.run("fib(10)")
    # cProfile.run("fib(15)")
    # cProfile.run("fib(20)")
    # cProfile.run("fib(25)")
    # cProfile.run("fib(50)")
    # cProfile.run("fib(100)")
    # cProfile.run("fib(500)")
    # cProfile.run("fib(1000)")
    # cProfile.run("fib_bin(5)")
    # cProfile.run("fib_bin(10)")
    # cProfile.run("fib_bin(15)")
    # cProfile.run("fib_bin(20)")
    # cProfile.run("fib_bin(25)")
    # cProfile.run("fib_bin(50)")
    # cProfile.run("fib_bin(100)")
    # cProfile.run("fib_bin(500)")
    # cProfile.run("fib_bin(1000)")
    # cProfile.run("sum_series_for_with_iterator(5)")
    # cProfile.run("sum_series_for_with_iterator(10)")
    # cProfile.run("sum_series_for_with_iterator(50)")
    # cProfile.run("sum_series_for_with_iterator(100)")
    # cProfile.run("sum_series_for_with_iterator(500)")
    # cProfile.run("sum_series_for_with_iterator(1000)")
    # cProfile.run("sum_series_while(5)")
    # cProfile.run("sum_series_while(10)")
    # cProfile.run("sum_series_while(50)")
    # cProfile.run("sum_series_while(100)")
    # cProfile.run("sum_series_while(500)")
    # cProfile.run("sum_series_while(1000)")
    # cProfile.run("sum_series_form(5)")
    # cProfile.run("sum_series_form(10)")
    # cProfile.run("sum_series_form(50)")
    # cProfile.run("sum_series_form(100)")
    # cProfile.run("sum_series_form(500)")
    # cProfile.run("sum_series_form(1000)")
