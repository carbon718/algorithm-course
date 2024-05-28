import figures

circle = figures.Circle(1)
print("koło pole: ", circle.area())
print("koło obwód: ", circle.perimeter())

square = figures.Square(1)
print("kwadrat pole: ", square.area())
print("kwadrat obwód: ", square.perimeter())

triangle = figures.Triangle(3, 4, 5)
print("trójkąt pole: ", triangle.area())
print("trójkąt obwód: ", triangle.perimeter())