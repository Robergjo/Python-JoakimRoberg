from Labb3_figurer import Rectangle, Circle

# geometriska figurer

rectangle1 = Rectangle(x=3, y=1, side1=5, side2=3)
rectangle2 = Rectangle(x=1, y=1, side1=2, side2=3)
circle1 = Circle(x=0, y=0, radius=1)
circle2 = Circle(x=1, y=1, radius=1)

# testa area och omkrets
print("============================================")
print("Rectangle 1 perimiter:", rectangle1.perimeter)
print("Rectangle 1 area:", rectangle1.area)
print("Rectangle 2 perimiter:", rectangle2.perimeter)
print("Rectangle 2 area:", rectangle2.area)
print("Circle 1 perimeter:", circle1.perimeter)
print("Circle 1 area:", circle1.area)
print("Circle 2 perimeter:", circle2.perimeter)
print("Circle 2 area:", circle2.area)
print("============================================")
print("Rectangle 1 is equal to Rectangle 2:", rectangle1 == rectangle2)
print("Circle 1 is equal to Circle 2:", circle1 == circle2)
print("Rectangle 1 is less than Rectangle 2:", rectangle1 < rectangle2)
print("Circle 1 is greater than Circle 2:", circle1 > circle2)
print("============================================")
# Kontrolleerra om punkterna ligger inom figurerna
print("Point (2, 2) is inside Rectangle 1:", rectangle1.is_inside(2, 2))
print("Point (1, 4) is inside Rectangle 2:", rectangle2.is_inside(1, 4))
print("Point (0, 0) is inside Circle 1:", circle1.is_inside(0, 0))
print("Point (0.5, 0.5) is inside Circle 2:", circle2.is_inside(0.5, 0.5))
print("--------------------------------------------")
print("Moving figures")
print("--------------------------------------------")

# Flytta figurer
rectangle1.translate(1, 1)
rectangle2.translate(2, 2)
circle1.translate(-1, -1)
circle2.translate(5, 5)

print("============================================")
# Kontrollera om punkter ligger inuti figurer
print("Point (2, 2) is inside Rectangle 1:", rectangle1.is_inside(2, 2))
print("Point (1, 4) is inside Rectanglee 2:", rectangle2.is_inside(1, 4))
print("Point (0, 0) is inside Circle 1:", circle1.is_inside(0, 0))
print("Point (0.5, 0.5) is inside Circle 2:", circle2.is_inside(0.5, 0.5))

print("============================================")
# Kontrollera om det är en enhetscirkel eller kvadrat
print("Circle 1 is a unit circle:", circle1.is_unit_circle())
print("Rectangle 1 is a square:", rectangle1.is_square())

print("============================================")
