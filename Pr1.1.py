time = int(input("Введите время в секундах"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
sec = time - hours * 3600 - minutes * 60
t = (
    f"{hours}:"
    f"{minutes}:"
    f"{sec}."
)
print(t)
