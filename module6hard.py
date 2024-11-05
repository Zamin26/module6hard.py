import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)  # список цветов
        self.__sides = list(sides)  # список сторон
        self.filled = True  # закрашенный

    def get_color(self):  # список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= i <= 255 for i in (r, g, b))  # принимает параметры r, g, b

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):  # принимает параметры r, g, b - числа и изменяет атрибут __color, в списке*
            self.__color = [r, g, b]
        # else: print("Некорректный цвет, без изменений.")

    def __is_valid_sides(self, *new_sides):
        if (side > 0 for side in new_sides) and len(new_sides) == self.sides_count:  # неограниченное кол-во сторон
            return True
        # else:
        # False

    def get_sides(self):  # возвращает значение атрибута __sides
        return self.__sides

    def __len__(self):  # периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # новые стороны
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        # else:
        # print("Стороны некорректны.")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):  # Площадь круга
        __radius = self.sides / 2
        print(3.14 * (__radius ** 2))  # pR^2


class Triangle:
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(self, color, *sides)

    def get_square(self):  # площадь треугольника
        r, g, b = self.sides
        s = (r + g + b) * 0.5
        return math.sqrt(s * (s - r) * (s - g) * (s - b))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            super().__init__(color, *([1] * self.sides_count))
        else:
            super().__init__(color, *([sides[0]] * self.sides_count))

    def get_volume(self):                       # объём куба
        side = self.get_sides()[0]
        return side ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
