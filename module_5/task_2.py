print('Задача 2. Максимум из трёх чисел')

# Как-то у нас уже было задание на нахождение максимума из трёх чисел с
# помощью дополнительной переменной. Теперь, когда вы знаете намного больше,
# вы можете оптимизировать программу, не тратя память компьютера на лишние
# переменные.

# Напишите программу, которая находит максимум из трёх чисел, не используя
# дополнительные переменные.

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
if num_2 < num_1 > num_3:
    print('Максимальное число:', num_1)
elif num_1 < num_2 > num_3:
    print('Максимальное число:', num_2)
else:
    print('Максимальное число:', num_3)