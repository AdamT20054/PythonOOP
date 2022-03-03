class Vehicle:
    
    def __init__(self, mspeed, milage):
        self.mSpeed = mspeed
        self.milage = milage
        
        
    def show(self):
        print("Max speed:", self.mSpeed, "\nMilage:", self.milage)
        
        
car = Vehicle(250, 50000)
car.show()
