# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

# 1 - 0
# 2 - 12 - 1 - #1 + 1
# 3 - 12 23 13 - 3 - #2 + 2
# 4 - 12 13 14 23 24 34 - 6 - #3 + 3
# 5 - 12 23 13 34 14 24 45 15 25 35 - 10 #4 + 4
# 6 - 12 23 13 34 14 24 45 15 25 35 56 16 26 36 46 - 15 - #5+ 5
# 7 - 12 23 13 34 14 24 45 15 25 35 56 16 26 36 46 67 17 27 37 47 57 - 21 - #6+5

# f(n) = f(n-1) + n-1


def input_count_friends():
    while True:
        number = input("Пожалуйста, введите количество друзей: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
        print("Ошибка ввода количества друзей.")


def test_count_handshakes(fun):
    assert 0 == fun(1)
    assert 1 == fun(2)
    assert 3 == fun(3)
    assert 6 == fun(4)
    assert 10 == fun(5)
    assert 15 == fun(6)
    assert 21 == fun(7)


def count_handshakes_graph(n):
    graph = [[j != i for j in range(n)] for i in range(n)]
    count_handshake = 0
    for i in range(n):
        for j in range(i, n):
            count_handshake += graph[i][j]
    return count_handshake


def count_handshakes_line(n):
    sum_handshake = 0
    for i in range(0, n):
        sum_handshake = sum_handshake + i
    return sum_handshake


if __name__ == "__main__":
    test_count_handshakes(count_handshakes_graph)
    test_count_handshakes(count_handshakes_line)
    count_friends = input_count_friends()
    print(f"Подсчет рукопожатий через граф для {count_friends} друзей: {count_handshakes_graph(count_friends)}")
    print(f"Подсчет рукопожатий через динамическое программирование для {count_friends} друзей: "
          f"{count_handshakes_line(count_friends)}")
