# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
def test_prime(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert lst == func(50)


def eratosthenes(n):
    """
    Метод поиска простых чисел методом "Решето Эратосфена".
    :param n: до какого числа идет поиск чисел.
    :return: список простых чисел от 1 до n.
    """
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return [x for x in sieve if x != 0]


# eratosthenes(100): 1000 loops, best of 5: 23.6 usec per loop
# eratosthenes(200): 1000 loops, best of 5: 42.2 usec per loop
# eratosthenes(300): 1000 loops, best of 5: 64.6 usec per loop
# eratosthenes(400): 1000 loops, best of 5: 95 usec per loop
# eratosthenes(500): 1000 loops, best of 5: 124 usec per loop
# Сложность алгоритма составляет O(n*log(log n)), при этом, для хранения информации о том,
# какие числа были вычеркнуты требуется O(n) памяти
def simple(n):
    """
    Метод поиска простых чисел методом "Решето Эратосфена".
    :param n: до какого числа идет поиск чисел.
    :return: список простых чисел от 1 до n.
    """
    primes = [2]
    for i in range(3, n + 1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


# simple(100): 1000 loops, best of 5: 30 usec per loop
# simple(200): 1000 loops, best of 5: 81.9 usec per loop
# simple(300): 1000 loops, best of 5: 157 usec per loop
# simple(400): 1000 loops, best of 5: 232 usec per loop
# simple(500): 1000 loops, best of 5: 341 usec per loop
# Прямой перебор позволяет уменьшить необходимое количество памяти за счет существенного увеличения времени нахождения
# числа (O(N^2))
if __name__ == "__main__":
    test_prime(eratosthenes)
    test_prime(simple)
