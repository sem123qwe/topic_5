days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

request = int(input("Введите номер дня недели от 1 до 7: "))

operation = days[request - 1]

print(operation)