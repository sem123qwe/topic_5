fruits = dict(яблоки = 50, банан = 30, груша = 40, апельсин = 35)

print("Список фруктов и их цены:")
print(fruits)  

user_input = input('Выберите фрукт из списка: ')  

price = fruits[user_input]
print('Цена груша -', price)  
