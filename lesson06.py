# Задание1
# переключение между режимами светофора
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(6)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()

# Задание 2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * 125 / 1000

class MassCount(Road):
    def __init__(self, _length, _width, thick):
        super(). __init__(_length, _width)
        self.thick = thick

m1 = MassCount(20, 5000, 125)
print(m1.mass())

# Задание 3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_ful_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

s = Position("Ivan", "Ivanov", "Manager", 500000, 100000)
print(s.get_ful_name())
print(s.position)
print(s.get_total_income())

# Задание 4

class Car:
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, limit_speed):
        super().__init__(speed, color, name, limit_speed)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} {self.speed}')

        if self.speed > 60:
            return f'{self.name} превысил допустимую скорость для городского автомобиля'

        else:
            return f'{self.name} это допустимая скорость для городского автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}  {self.speed}')

        if self.speed > 40:
            return f'{self.name} превысил допустимую скорость для городского автомобиля'
        else:
            return f'{self.name} это допустимая скорость для городского автомобиля'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейский автомобиль'
        else:
            return f'{self.name} это не полицейский автомобиль'

bmw = SportCar(110, 'Красный', 'BMW', False)
kia = TownCar(40, 'Белый', 'Kia', False)
lada = WorkCar(70, 'Зеленый', 'Lada', True)
ford = PoliceCar(110, 'Синий',  'Ford', True)
print(lada.turn_left())
print(f'Когда {kia.turn_right()}, затем {bmw.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name}  {lada.color}')
print(f'Is {bmw.name} полицейский автомобиль? {bmw.is_police}')
print(f'Is {lada.name}  полицейский автомобиль? {lada.is_police}')
print(bmw.show_speed())
print(kia.show_speed())
print(ford.police())
print(ford.show_speed())

# Задание 5

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Запуск отрисовки карандашом {self.title}')


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f'Запуск отрисовки маркером {self.title}')


pen = Pen('Отрисовка ручкой')
pencil = Pencil('Отрисовка карандашом')
handle = Handle('Отрисовка маркером')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

