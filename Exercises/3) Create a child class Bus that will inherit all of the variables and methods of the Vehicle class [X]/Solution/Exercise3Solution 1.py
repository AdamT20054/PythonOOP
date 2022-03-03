class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("Volvo", 140, 120000)
print("Vehicle Name:", School_bus.name, "\nSpeed:", School_bus.max_speed, "\nMileage:", School_bus.mileage)