# year = int(input('Введите дату выпуска: '))
# speed_count = int(input('Введите количество скоростей: '))
# if year >= 2018 and speed_count >= 24:
#     print('Подходит')
# else:
#     print('Не соответствует критериям')

# Второй вариант решения задачи

year = int(input('Введите дату выпуска: '))
speed_count = int(input('Введите количество скоростей: '))
if year < 2018 or speed_count < 24:
    print('Не соответствует критериям')
else:
    print('Подходит')
