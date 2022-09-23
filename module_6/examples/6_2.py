# password = int(input('Введите пароль: '))
# while password != 235:
#     print('Неверный пароль!')
#     password = int(input('Попробуйте еще раз: '))
# print('Пароль верный. Добро пожаловать!')

balance = int(input('Сколько денег пришло? '))
while balance > 5000:
    product_cost = int(input('Введите стоимость товара: '))
    balance -= product_cost
print('Внимание! На карте осталось мало денег! Остановитесь!')
print('Баланс счета:', balance)
