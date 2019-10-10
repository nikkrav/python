entered = int(input("Введите целое положительное число"))
maximum = entered % 10
entered = entered // 10
while entered > 0:
    if entered % 10 > maximum:
        maximum = entered % 10
        entered = entered // 10
    else:
        entered = entered // 10
print("Наибольшая цифра, в введенном Вами числе: " + str(maximum))


