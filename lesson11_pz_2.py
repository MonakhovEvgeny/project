class Zero:
    x = float(input('Введите число - '))
    y = float(input('Введите делитель - '))
    try:
        x / y
    except:
        print('Деление на ноль не представляется возможным')
    else:
        print(x, '/', y, '=', x / y)

Zero()