"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой
строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

string = input("Введите строку из нескольких слов, разделенных пробелами")
string = string.split() # Разделение на элементы
length = len(string)
i = 0
while i < length:
    if len(string[i]) > 10:
        string[i] = string[i][0:10] # Ограничение на 10 символов
    print(str((i + 1)) + " " + string[i])
    i += 1