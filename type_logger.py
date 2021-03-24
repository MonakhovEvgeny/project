def type_logger(func):
    def wrapper(x, y, z):
        print(f'{func.__name__}, {x}: {type(x)}, {y}: {type(y)}, {z}: {type(z)}')
        func(x, y, z)

    return wrapper


@type_logger
def positional_arg(x, y, z):
    return x, y, z

positional_arg(4, 3.65, 'Hello')



