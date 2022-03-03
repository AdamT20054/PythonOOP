class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        print("The seating capacity of a", self.name, "is", capacity, "passengers")
    
    
class Bus(Vehicle):
    
    # Assign default value to capacity should a value not be passed in.
    def seating_capacity(self, capacity=50):
        # The super() function is used to give access to methods and properties of a parent or sibling class.
        # The super() function returns an object that represents the parent class.
        print(super().seating_capacity(capacity))
    

School_bus = Bus("Volvo", 140, 200000)

# No value passed in, output will be 50
School_bus.seating_capacity()

# Value passed in, output will be 45
School_bus.seating_capacity(45)
