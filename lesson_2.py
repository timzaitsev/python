print('Задание 4')
sentence = input('Введите предложение: ')
phrase = sentence.split()
for ind,el in enumerate(phrase,1):
    print(ind,el)
print('Задание 3 словарь')
month = input('Введите номер месяца (1 - 12): ')
year = dict (key_1 = 'зима',key_2 = 'зима',key_3 = 'весна',key_4 = 'весна',key_5 = 'весна',key_6 = 'лето',key_7 = 'лето',key_8 = 'лето',key_9 = 'осень',key_10 = 'осень',key_11 = 'осень',key_12 = 'зима')
if year.get('key_' + month) == None:
    print('Введено неверное значение')
else:
    print(year.get('key_' + month))
print('Задание 3 список')
month = input('Введите номер месяца (1 - 12): ')
year = ['12','1','2','3','4','5','6','7','8','9','10','11']
if (month in year) == True:
    pos = year.index(month)
    if pos <= 2:
        print('Зима')
    elif 5 >= pos > 2:
        print('Весна')
    elif 8 >= pos > 5:
        print('Лето')
    elif 11 >= pos > 8:
        print('Осень')
else:
    print('Введено неверное значение')
print('Задание 2')
un = 0
new_list = []
while exit != 110:
    un = un + 1
    new_el = input('Введите элемент списка: ')
    new_list.append(new_el)
    exit = int(ord(input('Продолжить ввод? (y/n)')))
print( 'Первоначальный список', new_list)
if un == 1:
    print('Преобразованный список', new_list)
elif un%2 == 0 and un >= 4:
    a = new_list[0]
    b = new_list[1]
    c = new_list[2]
    d = new_list[3]
    new_list.pop(3)
    new_list.pop(2)
    new_list.pop(1)
    new_list.pop(0)
    new_list.insert(0, b)
    new_list.insert(1, a)
    new_list.insert(2, d)
    new_list.insert(3, c)
    print('Преобразованный список', new_list)
else:
    a = new_list[0]
    b = new_list[1]
    new_list.pop(0)
    new_list.pop(1)
    new_list.insert(0, b)
    new_list.insert(1, a)
    print('Преобразованный список', new_list)
print('Задание 1')
my_list = [12,'hello',23.5,None,-567,'Happy Day']
for el in  my_list:
    print(el, ':', type(el))

