"задание 6"
print('Задание 6')
first_day = abs(float(input("Расстояние начальное в километрах: ")))
countdown_day = abs(float(input("Расстояние желаемое в километрах: ")))
day = 1
progress = first_day
while progress <= countdown_day:
    day = day + 1
    progress = progress + (progress / 10)
print('Желаемое расстояние будет достигнуто на', day,'день')
"задание 5"
print('Задание 5')
takings = abs(int(float(input("Введите значение выручки в рублях:"))))
costs = abs(int(float(input("Введите значение издержек в рублях:"))))
if takings > costs:
    profit = takings - costs
    efficiency = (profit / takings) * 100.0
    print('Предприятие получило прибыль', profit,'руб')
    print('Рентабельность составила', efficiency,'%')
    employee = abs(int(float(input("Введите количество ссотрудников:"))))
    prof_to_emp = profit / employee
    print('Прибыль на 1 сотрудника составила',prof_to_emp,'руб')
elif takings == costs:
    print('Прибыль предприятия составила 0 рублей')
else:
    print('Предприятие сработало в убыток')
"задание 4"
print('Задание 4')
y = abs(int(float(input("Введите число:"))))
"определяем самую большую цифру в введённом числе"
z = 1
x = 0
m = y
l = 0
while (y // z) > 0:
    k = m % 10
    m = m // 10
    p = 0
    while k != p:
        p = p + 1
    if p > l:
        l = p
        k = 0
    x = x + 1
    z = 10 ** x
print(l,k,p,x,m,z)
"задание 3"
print('Задание 3')
n = abs(int(float(input("Введите число:"))))
"определяем количество разрядов в введённом числе"
a = 1
b = 0
c = 0
while (n // a) > 0:
    b = b + 1
    a = 10 ** b
    c = 100 ** b
nn = (n * (1 + a))
nnn = (n * (1 + a + c))
d = n + nn + nnn
print(n,'+',nn,'+',nnn,'=',d)
"задание 2"
print('Задание 2')
inp_time_sec = abs(int(float(input("Введите время в секундах:"))))
hours = inp_time_sec // 3600
time_inter = inp_time_sec - (hours * 3600)
minutes = time_inter // 60
seconds = time_inter - (minutes * 60)
print(hours,':',minutes,':',seconds)


