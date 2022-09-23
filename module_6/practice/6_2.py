# Задача 1. Циклы — это сложно?

summ = 0
number = int(input('Введите число: '))
while number != 0:
    summ += number
    number = int(input('Введите число: '))
print(summ)
