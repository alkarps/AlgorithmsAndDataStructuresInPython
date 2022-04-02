# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
# считается не решённой.
from hashlib import sha1


def test_count_substrings_in_string(fun):
    datas = (("123", 5), ("1223", 9))
    for data, expected in datas:
        actual = fun(data)
        assert expected == actual, f"{expected}!={actual} for {data}"


def cal_count_substrings_in_string(data, substring=None):
    def __hash(string):
        return sha1(string.encode("utf-8")).hexdigest()

    assert len(data) > 0 and (substring is None or len(substring) > 0)
    assert substring is None or len(data) >= len(substring)
    count = 0
    len_data = len(data)
    if substring is None:
        uniq_substr = set()
        for size in range(1, len_data):
            for i in range(len_data - size + 1):
                substring = data[i:i + size]
                if substring not in uniq_substr:
                    uniq_substr.add(substring)
                    count += cal_count_substrings_in_string(data, substring)
    else:
        len_sub = len(substring)
        hash_sub = __hash(substring)
        for i in range(len_data - len_sub + 1):
            temp = data[i:i + len_sub]
            if hash_sub == __hash(temp) and temp == substring:
                count += 1
    return count


if __name__ == "__main__":
    test_count_substrings_in_string(cal_count_substrings_in_string)
    print(cal_count_substrings_in_string("dawrhg42"))
