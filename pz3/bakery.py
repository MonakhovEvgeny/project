with open('sum.txt', 'w') as s: pass    # стираем все данные из файла чтобы при следующих
                                        # запусках не мешали
el = ()
while el != 'q':
    el = input('Введите сумму (для завершения ввода нажмите "q" - ')
    if el == 'q':
        break
    with open('sum.txt', 'a') as s:
        s.write(el + '\n')


# with open('sum.txt', 'r',) as si:
#     print(*si)


