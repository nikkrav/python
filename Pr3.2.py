def user():
    name = input("Введите имя пользователя")
    surname = input("Введите фамилию пользователя")
    year = input("Введите год рождения пользователя")
    city = input("Введите название города проживания пользователя")
    mail = input("Какой адрес электронной почты у пользователя?")
    phone = input("Введите номер телефона пользователя")
    data = (name, surname, year, city, mail, phone)
    return data


res = str(user())
print("Информация по пользователю: " + res)
