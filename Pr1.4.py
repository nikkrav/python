revenue = int(input("Введите значение выручки фирмы"))
costs = int(input("Введите значние издержек за этот же период"))
if revenue > costs:
    print("Фирма работает с прибылью")
    profit = revenue - costs
    profitability = profit / revenue
    print("Рентабельность фирмы составляет: " + ("%.2f" % profitability))
    n = int(input("Сколько человек в фирме?"))
    print("Прибыль на одного рабочего фирмы составляет: " + str("%.2f" % (profit / n)))
elif revenue == costs:
    print("Компания работает в ноль")
else:
    print("Фирма работает в убыток")