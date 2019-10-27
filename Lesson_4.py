print('Задание 5')
from functools import reduce
massive = [a for a in range(100,1002,2)]
print(massive)
print(reduce(lambda x, a: a * x, massive))
print('Задание 4')
from random import randint
first_data = [randint(0,100) for _ in range(30)]
print(first_data)
second_data = [el for el in first_data if first_data.count(el) == 1]
print(second_data)
third_data = [un for un in first_data if first_data.count(un) > 1]
print(third_data)
print('Задание 3')
price = [num for num in range(20,241,1) if num % 20 == 0 or num % 21 == 0]
print(price)
print('Задание 2')
from random import randint
list = []
sec_list = []
i = 0
while i != 10:
    n = randint(0,100)
    list.insert(i,n)
    i += 1
print(list)
sec_list.append(list[0])
a = 1
b = 0
while a != i:
    if list[a] > list[b]:
        sec_list.append(list[a])
    a += 1
    b += 1
print(sec_list)
""""
i = 0
while i != 10:
    i += 1
    list.append(randint(0,100))
"""

