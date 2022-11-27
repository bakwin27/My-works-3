import math
class Romb:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def printer(self):
        S = (self.x*self.y)/2
        print('Площадь ромба:', S)
        p = 2 * math.sqrt(self.x**2 + self.y**2)
        print('Периметр:', p)
    def printer2(self):
        S = self.x * self.y
        print('Площадь ромба:', S)
        P = self.x * self.y
        print('Периметр:', P)
class Paral:
    def __init__(ss,a,b,c):
        ss.a = a
        ss.b = b
        ss.c = c
    def printer(ss):
        S = 2*(ss.a*ss.b + ss.a*ss.c + ss.b*ss.c)
        print('Площадь параллелепипеда:', S)
        P = 4*(ss.a + ss.b + ss.c)
        print('Периметр:', P)
class Ellips:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def printer(self):
        S = math.pi * (self.a * self.b) / 4
        print('Площадь эллипса:', S)
        P = 2*math.pi*math.sqrt((self.a**2 + self.b**2)/8)
        print('Периметр:', P)
    def printer2(self):
        S = math.pi * self.a * self.b
        print('Площадь эллипса:', S)
        P = 2*math.pi*math.sqrt((self.a**2 + self.b**2)/2)
        print('Периметр:', P)