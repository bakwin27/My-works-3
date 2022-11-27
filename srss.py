import srs

       
i = input('R: 1  P: 2  E: 3\n')
if i == '1':
    ee = input('d: 1  h: 2\n')
    if ee == '1':
        a = int(input('d₁ :'))
        b = int(input('d₂ :'))
        r = srs.Romb(a,b)
        r.printer()
    elif ee == '2':
        a = int(input('Сторона a:'))
        d = int(input('Высота :'))
        r = srs.Romb(a,d)
        r.printer2()
elif i == '2':
    a = int(input('Длина ребра параллелепипеда а: '))
    b = int(input('Длина ребра параллелепипеда b: '))
    c = int(input('Длина ребра параллелепипеда c: '))
    P = srs.Paral(a, b, c)
    P.printer()
elif i == '3':
    ee = input('Оси: 1  полуОси: 2\n')
    if ee == '1':
        a = int(input('Большая ось: '))
        b = int(input('Малая ось: '))
        e = srs.Ellips(a,b)
        e.printer()
    elif ee == '2':
        a = int(input('Большая полуось: '))
        b = int(input('Малая полуось: '))
        e = srs.Ellips(a,b)
        e.printer2()