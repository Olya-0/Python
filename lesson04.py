# Задание 1

from sys import argv

script, work_hour, rate, bonus = 'argv', 'work_hour', 'rate', 'bonus'
print(f'ar1: {argv[1]}')
print(f'ar2: {argv[2]}')
print(f'ar3: {argv[3]}')

salary = (int(work_hour) * int(rate) + int(bonus))
print(f'Ваша зарплата {salary}')

# Задание 2

my_list = [1, 2, 10, 5, 15, 3, 200,50, 75]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)

# Задание 3

num = range(20, 240)
new_list = [el for el in num if el%20==0 or el%21==0]
print(new_list)

# Задание 4

my_list2 = [1, 5, 1, 25, 25, 85, 5, 10, 25]
new_2 = [el for el in my_list2 if my_list2.count(el)==1]
print(new_2)

# Задание 5

from functools import reduce

new_list_3 = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, new_list_3))




