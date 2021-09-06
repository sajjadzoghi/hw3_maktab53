from math import sqrt


class Shape:
    def __init__(self, lenght=None, height=None, width=None):
        self.lenght = lenght
        self.height = height
        self.width = width


class Rectangle(Shape):
    def __init__(self, length, width, height=None):
        super().__init__(length, height, width)

    def area(self):
        if self.lenght > 0 and self.width > 0:
            return f'area = {self.lenght * self.width}'
        else:
            return 'Sorry! One of width or lenght has an invalid value.'

    def perimeter(self):
        if self.lenght > 0 and self.width > 0:
            return f'perimeter = {2 * (self.lenght + self.width)}'
        else:
            return 'Sorry! One of width or lenght has an invalid value.'

    def display(self):
        if self.lenght > 0 and self.width > 0:
            for _ in range(self.width):
                print('*' * self.lenght)
        else:
            print('Sorry! One of width or lenght has an invalid value.')


class Parallelogram(Shape):
    def __init__(self, length, height):
        super().__init__(length, height)

    def area(self):
        if self.lenght > 0 and self.height > 0:
            return f'area = {self.lenght * self.height}'
        else:
            return 'Sorry! One of height or lenght has an invalid value.'

    def perimeter(self):
        if self.lenght > 0 and self.height > 0:
            return f'perimeter = {2 * (self.lenght + (self.height * sqrt(2)))}'
        else:
            return 'Sorry! One of height or lenght has an invalid value.'

    def display(self):
        if self.lenght > 0 and self.height > 0:
            for i in range(1, self.height + 1):
                print((self.height - i) * ' ' + (self.lenght * '*'))
        else:
            print('Sorry! One of height or lenght has an invalid value.')


class Rhombus(Parallelogram):
    def __init__(self, length, height=None):
        super().__init__(length, height)

    def area(self):
        if self.lenght > 0:
            return f'area = {self.lenght * (self.lenght / sqrt(2))}'
        else:
            return 'Sorry! lenght has an invalid value.'

    def perimeter(self):
        if self.lenght > 0:
            return f'perimeter = {4 * self.lenght}'
        else:
            return 'Sorry! lenght has an invalid value.'

    def display(self):
        if self.lenght > 0:
            height = round(self.lenght / sqrt(2))
            for i in range(1, height + 1):
                print((height - i) * ' ' + (self.lenght * '*'))
        else:
            print('Sorry! lenght has an invalid value.')


class Square(Rectangle):
    def __init__(self, length, width=None):
        super().__init__(length, width)

    def area(self):
        if self.lenght > 0:
            return f'area = {self.lenght ** 2}'
        else:
            return 'Sorry! lenght has an invalid value.'

    def perimeter(self):
        if self.lenght > 0:
            return f'perimeter = {4 * self.lenght}'
        else:
            return 'Sorry! lenght has an invalid value.'

    def display(self):
        if self.lenght > 0:
            for _ in range(self.lenght):
                print('*' * self.lenght)
        else:
            print('Sorry! lenght has an invalid value.')


class Diamond(Square):
    def __init__(self, *args):
        super().__init__(*args)

    def display(self):
        if self.lenght > 0:
            for i in range(1, self.lenght + 1):
                print(' ' * (self.lenght - i), '*' * (i * 2 - 1))
            for i in range(self.lenght - 1, -1, -1):
                print(' ' * (self.lenght - i), '*' * (i * 2 - 1))
        else:
            print('Sorry! lenght has an invalid value.')


sq1 = Square(8)
print(sq1.area())
dia1 = Diamond(5)
print(dia1.perimeter())
rho1 = Rhombus(4)
print(rho1.perimeter())
rect1 = Rectangle(4, 3)
print(rect1.perimeter())
para1 = Parallelogram(6, 4)
print(para1.area())
print(para1.perimeter())
rect1.display()
para1.display()
rho1.display()
dia1.display()
