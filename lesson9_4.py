class Car:
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police
    
  def go(self):
    return f'the car went'
    
  def stop(self):
    return f'the car stopped'
    
  def turn(self):
    return f'the car turned'
    
  def show_speed(self):
    return print('speed', self.speed)
    
    
class TownCar(Car):
  def show_speed(self):
    if self.speed > 60:
      print('I stopped you for speeding')
    else: print('your speed - ', self.speed)
    
    
class SportCar(Car):
  pass
  
  
class WorkCar(Car):
  def show_speed(self):
    if self.speed > 40:
      print('I stopped you for speeding')
    else: print('your speed - ', self.speed)
  
  
class PoliceCar(Car):
  pass
    

car1 = TownCar(65, 'red', 'bmv', True)
car1.show_speed()
print(car1.name, car1.color)

car2 = WorkCar(45, 'green', 'mazda', False)
car2.show_speed()

car2 = WorkCar(30, 'green', 'mazda', False)
car2.show_speed()
print(car2.turn())
