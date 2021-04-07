def tr():
    n = int(input('Введите кол-во строк в матрице - '))
    # a = []
    # a.append(n)
    list_1 = []
    for i in range(n):
        print(f'Введите  числа {i + 1} строки  через пробел и нажмите Enter')
        row = input().split()
        for i in range(len(row)):
            row[i] = row[i]
        list_1.append(row)
    # a.append(list_1)
    return list_1


class Matrix:

    def __init__(self, list_1):
        # self.n = a[0]
        self.list_1 = list_1

    def __str__(self):
        x = 0
        res = []
        fin = []

        for el in self.list_1:
            for i in el:
                if x < len(str(i)):
                    x = len(str(i))

            h = []

            for j in el:
                y = x - len(j)
                j = j + y * ' '
                h.append(j)
            res.append(h)
        for i in range(len(self.list_1)):
            s = ' '.join(map(str, res[i]))
            fin.append(s)
        fins = '\n'.join(map(str, fin))
        return f'Ваша матрица\n{fins}'

    def __add__(self, other):
        res = []

        p = abs(len(self.list_1) - len(other.list_1))
        for i in range(p):
            if len(self.list_1) < len(other.list_1):
                self.list_1.append(['0'])
            elif len(other.list_1) < len(self.list_1):
                other.list_1.append(['0'])
        x = 0
        for i in self.list_1:
            if x < len(i):
                x = len(i)
        for i in other.list_1:
            if x < len(i):
                x = len(i)
        for i in range(len(self.list_1)):
            while len(self.list_1[i]) < x:
                self.list_1[i].append('0')
        for i in range(len(other.list_1)):
            while len(other.list_1[i]) < x:
                other.list_1[i].append('0')
        for el in self.list_1:
            for i, elem in enumerate(el):
                el[i] = int(elem)
        for el in other.list_1:
            for i, elem in enumerate(el):
                el[i] = int(elem)
        for i in range(len(self.list_1)):
            res.append([x + y for x, y in zip(self.list_1[i], other.list_1[i])])
        for el in res:
            for i, elem in enumerate(el):
                el[i] = str(elem)
        return Matrix(res)


test = Matrix(tr())
print(test)
test1 = Matrix(tr())
print(test1)
print(test + test1)
