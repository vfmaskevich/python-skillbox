print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по
# полугодиям.
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух
# кварталов,
# чтобы понять динамику роста или падения дохода. И так за каждый год.
#
# Надя решила,
# что быстрее будет написать простую программу, которая сделает всё за неё.
#
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.

quarter_1 = int(input('Введите значение за 1 квартал: '))
quarter_2 = int(input('Введите значение за 2 квартал: '))
quarter_3 = int(input('Введите значение за 3 квартал: '))
quarter_4 = int(input('Введите значение за 4 квартал: '))
sum_1 = quarter_1 + quarter_2
sum_2 = quarter_3 + quarter_4
result = sum_1 / sum_2
print('Результат:', result)
