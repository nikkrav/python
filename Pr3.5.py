def func(*args):
    finalSum = 0
    specialSign = False
    try:
        for itm in args:
            finalSum += float(itm) if itm else 0
    except ValueError as e:
        specialSign = not specialSign
    return finalSum, specialSign


total = 0
while True:
    number = input("Введите числа через пробел. Для прекращения ввода введите что-то отличное от цифры").split(" ")
    finalSum, specialSign = func(*number)
    total += finalSum
    print(total)
    if specialSign:
        print("Вы закончили")
        break

