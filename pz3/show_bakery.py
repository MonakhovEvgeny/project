import sys
x = (sys.argv)

if len(x) == 1:
    with open('sum.txt', 'r', ) as si:
        print(*si)

if len(x) == 2:
    with open('sum.txt', 'r', ) as si:
        i = 0
        for line in si:
            i += 1
            if i >= int(x[1]):
                print(line)

if len(x) == 3:
    if int(x[2]) < int(x[1]):
        print('Введите корректные данные (первый аргумент не может быть больше второго)\n')
    with open('sum.txt', 'r', ) as si:
        i = 0
        for line in si:
            i += 1
            if i <= int(x[2]) and i >= int(x[1]):
                print(line)







