"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У
пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Например, набор натуральных чисел: 7, 5, 3, 3, 2. Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
"""
my_list = [7, 5, 3, 3, 2]
i = 0
nEl = int(input("Введите пожалуйста натуральное число"))
res = (my_list + [nEl]) # Присоединение элемента
res.sort() # Сортировка по возрастанию
res.reverse() # Теперь сортировка по убыванию
print(res)




