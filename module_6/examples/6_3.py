# # Задача «Погода для бега»
#
# weather = int(input('Сколько градусов на улице? '))
# meters = 0
# while weather > 15:
#     meters += 20    # Чуть пробежали вперед
#     weather -= 2    # Похолодало
#     if weather <= 15:
#         break
#     meters += 10    # Прошли немного пешком
# print('Пройдено метров: ', meters)

# Задача «Расшифровка кода»

number = int(input('Введите число: '))
summ = 0
while number != 0:
    last_num = number % 10
    print(last_num)
    if last_num == 5:
        print('Обнаружен разрыв')
        break
    summ += last_num
    number //= 10
print('Сумма: ', summ)
