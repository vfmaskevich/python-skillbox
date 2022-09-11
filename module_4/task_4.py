print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные
# комнаты. Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть. Вот для одного из таких магазинов он и написал
# калькулятор скидки, чтобы проще ориентироваться в ценах.

# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека.
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100).
# В конце вывести итоговую сумму на экран.

price_1 = int(input('Введите стоимость первого товара: '))
price_2 = int(input('Введите стоимость второго товара: '))
price_3 = int(input('Введите стоимость третьего товара: '))
sum_check = price_1 + price_2 + price_3
if sum_check >= 10000:
    result = sum_check - (sum_check * 10 / 100)
else:
    result = sum_check
print('Итоговая сумма равна:', result, 'руб.')