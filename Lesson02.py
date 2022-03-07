# Задание 1

name = 'Spisok'
li = [1, 30, 'Week', [1, 2, 3], name]
for i in li:
    print(type(i))

# Задание 2
# меняем местами соседние числа, если нечетное количество, последнее оставляем на месте

a = [int(i) for i in input('Введите число: ')]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

# Задание 3

number = int(input('Введите номер месяца: '))
if number <= 12 and number >= 1:
    month_dict = {1: 'Зима',
                  2: 'Зима',
                  3: 'Весна',
                  4: 'Весна',
                  5: 'Весна',
                  6: 'Лето',
                  7: 'Лето',
                  8: 'Лето',
                  9: 'Осень',
                  10: 'Осень',
                  11: 'Осень',
                  12: 'Зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Время года через list {month_list[i]}")
            break
    print(f"Время года через dict  {month_dict[number]}")
else:
    print("Ошибка: Такого месяца не существует")

# Задание 4

s = input('Введите слова: ')
a = s.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. {el}")

# Задание 5

number = int(input("Введите номер: "))
a = [7, 4, 3, 2]
c = a.count(number)
for element in a:
    if c > 0:
        i = a.index(number)
        a.insert(i+c, number)
        break
    else:
        if number > element:
            j = a.index(element)
            a.insert(j, number)
            break
        elif number < a[len(a) - 1]:
            a.append(number)
print(a)











