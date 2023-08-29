numbers = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]

# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
find_len = len(numbers)

find_sum = sum(numbers)

# Лишние скобки, а также можно сразу написать без переменных
calculation = (find_sum / find_len)

result = round(calculation, 1)

print('Среднее значение:', result)