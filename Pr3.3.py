def max():
    max1 = 0
    max2 = 0
    sum = 0
    fLetter = int(input("Введите первое число"))
    sLetter = int(input("Введите второе число"))
    tLetter = int(input("Введите третье число"))
    if fLetter <= sLetter and fLetter <= tLetter:
        max1 = sLetter
        max2 = tLetter
    elif sLetter <= fLetter and sLetter <= tLetter:
        max1 = fLetter
        max2 = tLetter
    else:
        max1 = sLetter
        max2 = fLetter
    sum = max1 + max2
    return sum


res = max()
print(str(res))