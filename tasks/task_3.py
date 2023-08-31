numbers: list = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]

calculation: float = sum(numbers) / len(numbers)  # делаем расчеты

result: float = round(calculation, 1)  # округляем результат расчетов

print('Среднее значение:', result)  # ввыводим результат