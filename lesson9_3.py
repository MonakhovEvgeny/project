class Worker:
    res = {}
    sum = 0
    def __init__(self, name, surname, position, _income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income
        self.res = {"wage": wage, "bonus": bonus}
        self.sum = _income + wage + bonus


class Position(Worker):

    def get_full_name(self):
        print(f'name: {self.name} surname: {self.surname}')

    def get_total_income(self):

        print(self.sum)


worker1 = Position('Ivan', 'Ivanov', 'rab', 90, 7, 8)
worker1.get_full_name()
worker1.get_total_income()
