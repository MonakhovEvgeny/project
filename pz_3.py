class Cell:
    __slots__ = ['number_cells']

    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __str__(self):
        return str(self.number_cells)

    def __add__(self, other):
        return f'Сумма ячеек исходных двух клеток - {Cell(self.number_cells + other.number_cells)}'

    def __sub__(self, other):
        res = self.number_cells - other.number_cells
        if res >= 0:
            return f'Клетка № 1 - клетка № 2: {Cell(res)}'
        else:
            return ('Разность количества ячеек двух клеток не может быть меньше нуля')

    def __mul__(self, other):
        return f'Умножение количества ячеек двух клеток - {Cell(self.number_cells * other.number_cells)}'

    def __floordiv__(self, other):
        return f'Результат целочисленного деления количества ячеек клетки № 1 на клетку № 2 - {Cell(self.number_cells // other.number_cells)}'

    def make_order(self, cells_in_row):
        print(f'Для {self.number_cells} ячеек, в {cells_in_row} ряда(-ов)')
        res = ''
        for i in range(self.number_cells // cells_in_row):
            res += ''.join(['*' for el in range(cells_in_row)]) + '\n'
        for _ in range(self.number_cells % cells_in_row):
            res += '*'
        return res


test1 = Cell(int(input('Введите количество ячеек клетки № 1 (целое число) - ')))
test2 = Cell(int(input('Введите количество ячеек клетки № 2 (целое число) - ')))
print(test1 + test2)
print(test1 - test2)

print(test1 * test2)
print(test1 // test2)
print(test1.make_order(int(input('Введите количество рядов клетки № 1 (целое число) - '))))
print(test2.make_order(int(input('Введите количество рядов клетки № 2 (целое число) - '))))