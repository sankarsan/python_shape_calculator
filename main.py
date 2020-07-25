from python_shape_calculator import shape_calculator as sc

rect = sc.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect.get_picture())
print(rect)
sq = sc.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq.get_picture())
print(sq)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

