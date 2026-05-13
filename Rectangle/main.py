from Rectangle import Rectangle

length = int(input("Enter length of rectangle"))
breadth = int(input("Enter breadth of rectangle"))

rectangle = Rectangle(length, breadth)

print(f"Area of rectangle : {rectangle.area()}")
print(f"Perimeter of rectangle: {rectangle.perimeter()}")