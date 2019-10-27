from sys import argv
production = int(argv[1])
tariff = int(argv[2])
bonus = int(argv[3])
salary = production * tariff + bonus
print(f'Выработка {production} часов * Ставка {tariff} рублей + Премия {bonus} рублей = Зарплата {salary} рублей')
