class Stationery:
  def __init__(self, title):
    self.title = title
    
  def draw(self):
    print('start rendering')
    
    
class Pen(Stationery):
  def draw(self):
    print('Song of the wolf')
    
    
class Pencil(Stationery):
  def draw(self):
    print('Duck song')
    
    
class Handle(Stationery):
  def draw(self):
    print('hedgehog song')
      
      

test1 = Stationery('book')
test2 = Pen('disk')
test3 = Pencil('newspaper')
test4 = Handle('poster')
test1 .draw()
test2 .draw()
test3 .draw()
test4 .draw()
  
