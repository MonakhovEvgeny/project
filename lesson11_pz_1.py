import re

class Data:
  str_date = input('Введите дату в формате день-месяц-год: ')
  def __init__(self, str_date):
    self.str_date = str_date
    
  @classmethod
  def number(cls):
    date = re.findall(r'\d+', cls.str_date)
    print('день - ', int(date[0]), '  месяц - ', int(date[1]), '  год - ', int(date[2]))
    return date
  
  
  @staticmethod
  def validation():
    valid = Data.number()
    if int(valid[0]) > 31 or int(valid[0]) < 0:
      print('Кол-во дней должно быть в пределах от 1 до 31')
    if int(valid[1]) > 12 or int(valid[1]) < 0:
      print('Кол-во месяцев должно быть в пределах от 1 до 12')
    if int(valid[2]) > 1999 or int(valid[2]) < 1900:
      print('Год должен быть в пределах XX века')
      
      
 
Data.number()
Data.validation()
