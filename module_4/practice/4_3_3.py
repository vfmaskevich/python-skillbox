# Задача 3. Угадай число 2.
#
# На удивление, отец и сын частенько стали играть в
# игру «Угадай число», и поэтому папа захотел немного усовершенствовать свою
# программу, чтобы на экран всегда выводилось нужное сообщение. Напишите
# программу, которая запрашивает число у пользователя, сравнивает его с
# другим числом и выводит соответствующее сообщение: «Угадал», — если они
# равны,  и: «Не угадал», — если не равны. В конце выводите фразу: «Конец
# игры».
#
# Пример 1:
# Какое число я загадал? 5
# Угадал!
# Конец игры
#
# Пример 2:
# Какое число я загадал? 6
# Не угадал!
# Конец игры
#
# Попробуйте решить задачу сначала с помощью одного знака сравнения (==),
# а затем с помощью другого (!=).

son = int(input('Какое число я загадал? '))
father = 5
if son == father:
    print('Угадал!')
if son != father:
    print('Не угадал!')
print('Конец игры')