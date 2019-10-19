dividend = float(input("Введите делимое число"))
while True:
    divider = float(input("Введите делитель"))
    if divider != 0:
        break
    else:
        print("Ошибка, деление на ноль. Введите другое значение делителя")


def division():
    res = dividend / divider
    return res


res = division()
print("Результат деления: " + str(round(res, 2)))