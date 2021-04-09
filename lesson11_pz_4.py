class Warehouse:
    pass


class Office_equipment:
    def __init__(self, manufacturer, price, model):
        self.manufacturer = manufacturer
        self.price = price
        self.model = model

class Printer(Office_equipment):
    def __init__(self, manufacturer, price, model):
        self.manufacturer = manufacturer
        self.price = price
        self.model = model

class Scanner(Office_equipment):
    def __init__(self, manufacturer, price, model):
        self.manufacturer = manufacturer
        self.price = price
        self.model = model



class Xerox(Office_equipment):
    def __init__(self, manufacturer, price, model):
        self.manufacturer = manufacturer
        self.price = price
        self.model = model
