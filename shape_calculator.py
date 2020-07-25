class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5


class Square(Rectangle):

    def __init__(self, side, width, height):
        super().__init__(side, side)
