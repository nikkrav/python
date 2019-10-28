"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_full_profit). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


n = "Иван"
s = "Иванов"
p = "Должность"
pr = 10
b = 40
class Worker:
    name = n
    surname = s
    position = p
    _pr = {"profit": pr, "bonus": b}
class Position:
    print("Полное имя сотрудника:" + Worker.name + " " + Worker.surname)
    print("Доход сотрудника составляет " + str(float(Worker._pr.get("profit")) + float(Worker._pr.get("bonus"))))