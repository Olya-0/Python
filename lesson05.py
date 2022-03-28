# Задание 1

my_func = open('new.txt', 'w')
line = input('Введите текст \n')
while line:
    my_func.writelines(line)
    line = input('Введите текст \n')
    if line == ' ':
        break

my_f.close()
my_f = open('new.txt', 'r')text = my_f.readlines()
print(text)
my_f.close()

# Задание 2

my_file = open('new1.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('new1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('new1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} строки {len(content[i])}')
my_file = open('new1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

# Задание 3

with open('salary.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

# Задание 4

translater = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('new2.txt', 'r') as file_obj:

   for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(translater[i[0]] + '  ' + i[1])
    print(new_file)

with open('new2.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# Задание 5

def summary():
    try:
        with open('new3.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_num = line.split()

            print(sum(map(int, my_num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно введен номер. Ошибка')
summary()
