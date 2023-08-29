colors: list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# Что если я добавлю/удалю элемент в/из списка?
colors[0], colors[5] = colors[5], colors[0]

print(colors)
