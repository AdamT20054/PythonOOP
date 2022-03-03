# "shape" is given from the object

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # Calculate area function made for Circle class.
    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)




class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    # Calculate area function made in Rectangle class.
    def calculate_area(self):
        print("Area of Rectangle :", self.length * self.width)

# Calculate area function are different in both classes.





# Area function takes parameter "shape"
def area(shape):
    # Call the instance method for the shape name.
    shape.calculate_area()

# Creates two shapes
cir = Circle(5)
rect = Rectangle(10, 5)

# Call the common function - the parameter given in this determines the which class the instance method comes from.
area(cir)
area(rect)