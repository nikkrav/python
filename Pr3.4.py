x = float(input("Введите число, которое возводится в степень"))
y = int(input("Введите показатель степени в виде целого, отрицательного числа"))


def my_func(x, y):
    i = 1
    res = 1
    for i in range(-y):
        res *= x
    return 1 / res


res = my_func(x, y)
print("Результат возведения в сепень (с точностью до четвертого знака после запятой) " + str(round(res, 4)))