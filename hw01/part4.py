# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
first_chr = ord(input("Введите первую букву: "))
second_chr = ord(input("Введите вторую букву: "))
a = ord("a")
z = ord("z")
if a <= first_chr <= z and a <= second_chr <= z:
    first_position = first_chr - a + 1
    second_position = second_chr - a + 1
    diff = max(second_position - first_position - 1, 0)
    print(f"Позиция первой буквы: {first_position}")
    print(f"Позиция второй буквы: {second_position}")
    print(f"Количество букв между первой и второй буквой: {diff}")
else:
    print("Ошибка ввода.")
