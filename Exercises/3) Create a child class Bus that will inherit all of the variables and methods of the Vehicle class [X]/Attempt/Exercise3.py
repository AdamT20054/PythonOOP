class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    
    def show(self):
        print("Vehicle Name:", self.name, "\nSpeed:", self.max_speed, "\nMileage:", self.mileage)
        
car = Bus("Volvo", 140, 120000)
car.show()