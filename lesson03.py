# Задание 1

def my_func (x, y):
    try:
        z = x/y
        return z
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return 'Введите число'
print(my_func(int(input('Введите x = ')), int(input('Введите y = '))))

# Задание 2

def my_func(Имя, Фамилия, Год, Город, email, Телефон):
    print(Имя, Фамилия, Год, Город, email, Телефон)

my_func(Имя = 'Ольга', Фамилия = 'Юнусова', Год = 1987, Город = 'Москва', email = 'email', Телефон = '8 (495) 111 - 11 - 11' )




# Задание 4

def my_func(x,y):
    return 1 / x ** abs(y)  # return x ** y
print(my_func(5, -4))

# Задание 5

import sys

result = 0

while True:
    line = input('Enter number or special token u for exit')
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'u':
                print(f'You sum is:{result}. Программа завершена')
                exit(0)
            else:
                print(f'Результат: {result}. Ошибка ввода')
                exit(1)

# Задание 3 (не по порядку)

def my_func(x, y,z):
    b = [x,y,z]
    total = []
    max_1 = max(b)
    total.append(max_1)
    b.remove(max_1)
    max_2 = max(b)
    total.append(max_2)
    print(sum(total))
my_func(-5,2,0)



