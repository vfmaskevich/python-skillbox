# # 4.3 Полная форма условного оператора if
# bank = int(input('Сколько денег на счету? '))
# if bank > 75000:
#     bank -= 75000
#     print('Курс успешно приобретен.')
# else:
#     print('Не хватает денег на счету.')
# print('Хорошего дня!')

apple = int(input('Доход от яблок: '))
orange = int(input('Доход от апельсинов: '))
expenses = int(input('Расходы: '))
if apple + orange > expenses:
    print('Доходы превышают расходы.')
else:
    print('Доход слишком мал.')
