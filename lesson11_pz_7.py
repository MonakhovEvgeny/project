class Complex_numbers:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.z = complex(self.x, self.y)
    print(self.z)
    
  def __add__(self, other):
    return (self.z + other.z)
    
  def __mul__(self, other):
    return (self.z * other.z)
    
    
    
    
test1 = Complex_numbers(2, 5)
test2 = Complex_numbers(3, 7)
print('Сумма введенных чисел и тип: ', test1 + test2, type(test1 + test2))
print('Произведение введенных чисел и тип: ', test1 * test2, type(test1 * test2))

