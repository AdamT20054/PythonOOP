# Inheritance is the process of inheriting properties of the parent class into a clild class.
# Eg; Car is a subclass of a Vehicle class.
# We can create a car by inheriting properties of a Vehicle such as Power, Weight and Acceleration and add extra properties as needed.

# Base class
class Vehicle:
    
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    # Child classes can not inherit private properties from the parent class
    def __private(self):
        print(self.name, "(Child class) can not inherit private properties")    
    
    def info(self):
        print("Model: ", self.name, "\nColor:", self.color, "\nPrice:", self.price)
        

# Child class
# Child class "Car" inherits all properties and functions of it's parent class (Vehicle)
class Car(Vehicle):
    
    # Within the child class, we can have seperate properties/functions.
    def change_gear(self, no):
        print(self.name, "changed gear to number", no)
        
car = Car("Koenigsegg Jesko", "White", 25000000)
car.info()
car.change_gear(5)
