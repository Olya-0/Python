# Задание 1

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[3, 10, 15],
                    [5, 12, 30],
                    [35, 50, 1]],
                    [[10, 2, 3],
                    [5, 7, 87],
                    [5, 4, 92]])


print(my_matrix.__add__())

# Задание 2


class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_square_c(self):
        return self.v / 6.5 + 0.5

    def get_square_j(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общий расход ткани \n'
                   f' {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.square_c}'

class Jacket(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_j = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.h * 2 + 0.3}'

coat = Coat(4, 3)
jacket = Jacket(5, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())

# Задание 3

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):

        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(15)
cells2 = Cell(12)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)




