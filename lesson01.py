# Задание 1

name = 'Olya'
print(name)
age = 13
print(age)


# Задание 2

s = int(input('Время в секундах '))
h = s//3600
m = (s-h*3600)//60
sec = s % 60
print(f'{h:02} : {m:02} : {sec:02}')

# Задание 3

n = input('Введите число: ')
print(int(n) + int(n + n) + int(n + n + n))

# Задание 4

num = int(input('Введите число: '))
maxi = 0
while num > 0:
    last_dig = num % 10
    if last_dig > maxi:
        maxi = last_dig
        if maxi == 9:
            break
    num //= 10
print('Максимальная цифра в числе -', maxi)

# Задание 5

tr = float(input('Введите вашу выручку: '))
tc = float(input('Введите ваши издержки: '))
p = tr - tc
if p > 0:
    print('Вы получили прибыль')
    print('Рентабельность: ', p/tr)
    i = int(input('Введите количество сотрудников'))
    print('Прибыль на одного сотрудника', p/i)
elif p == 0:
    print('Вы получаете нулевую прибыль')
else:
    print('Вы работаете  в убыток')


