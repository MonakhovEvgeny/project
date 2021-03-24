
def test12(y):
    def val_checker(func):
        def wrapper(arg):
            if y(arg) == True:
                print(func(arg))
            else:
                raise ValueError(f'ValueError: wrong val: {arg}')
        return wrapper
    return val_checker


@test12(lambda x: x > 0)
def test(arg):
    return arg
test(-5)



