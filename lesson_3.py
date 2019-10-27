#-------------------Четвёртое задание-------------------
print('Задание 4')
def neg_deg():
    try:
        x = float(input('Введите число '))
        y = int(input('Введите отрицательную степень числа '))
    except ValueError:
        print('Введено некорректное значение')
        return
    if y > 0:
        return print('Значение y должно быть отрицательным')
    z = 1
    h = x
    while z != abs(y):
        z += 1
        h *= x
    ant = 1 / h
    return x, y, z, h, ant
print(neg_deg())
#-------------------Третье задание-------------------
print('Задание 3')
def sum_to_max():
    try:
        a_1 = float(input('Введите первое число '))
        a_2 = float(input('Введите второе число '))
        a_3 = float(input('Введите третье число '))
    except ValueError:
        print('Введено некорректное значение')
        return
    list = [a_1, a_2, a_3]
    a = min(list)
    if list.index(a) == 0:
        max_2_sum = a_2 + a_3
    elif list.index(a) == 1:
        max_2_sum = a_1 + a_3
    elif list.index(a) == 2:
        max_2_sum = a_1 + a_2
    return max_2_sum
print(sum_to_max())
#-------------------Второе задание-------------------
print('Задание 2')
def card(**kwargs):
    return kwargs
print(card(Имя = input('Введите имя '), Фамилия = input('Введите фамилию '), Дата_рождения = input('Введите дату рождения '), Город = input('Введите город проживания '), email = input('Введите email '), phone = input('Введите омер телефона ')))
#-------------------Первое задание-------------------
print('Задание 1')
def divide(dividend, divider):
    try:
        private = float(dividend) / float(divider)
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
    except ValueError:
        print('Введено некорректное значение')
        return
    return private

arg_1 = input('введите делимое ')
arg_2 = input('введите делитель ')
print(divide(arg_1,arg_2))