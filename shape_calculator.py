class Rectangle:

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

    def get_picture(self):
        ret_val = "*" * self.width
        ret_val += "\n"
        ret_val = ret_val * self.height
        return  ret_val

    def get_amount_inside(self, shape):

        self_area = self.get_area()
        shape_area = shape.get_area()
        assert(self_area > shape_area)
        return self_area // shape_area

    def __str__(self):
        txt = "{classname} (width={width},height={height})"
        return txt.format(classname=self.__class__.__name__, width=self.width, height=self.height)


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        txt = "{classname} (side={side})"
        return txt.format(classname=self.__class__.__name__, side=self.width)
