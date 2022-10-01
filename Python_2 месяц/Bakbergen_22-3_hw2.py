class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * (self.__radius ** 2)

    def info(self):
        print(f"Circle radius: {self.__radius}, area: {self.calculate_area()}{self.unit}")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_b * self.__side_a / 2

    def info(self):
        print(f"Triangle side a: {self.__side_a}, side b: {self.__side_b}, area: {self.calculate_area()}{self.unit}.")


ciOne = Circle(8)
ciTwo = Circle(4)

trOne = RightTriangle(3, 6)
trTwo = RightTriangle(4, 9)
trTree = RightTriangle(2, 4)

general = [ciOne, ciTwo, trOne, trTwo, trTree]
for i in general:
    i.info()