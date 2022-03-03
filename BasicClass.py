class Employee: # Create class "Employee"
    
    # Class Variables - All objects created by this class have the same variables
    company_name = "Company 1"

    # Constructor to initialize the object - this is ran whenever an object is created.
    def __init__(self, name, salary):
        # Instance variables passed through the function parameters.
        self.name = name
        self.salary = salary
    
    # Instance method.
    def show(self):
        print("Employee:", self.name, self.salary, self.company_name)

# Create first object 
emp1 = Employee("Harry", 24000)
# Create second object
emp2 = Employee("Ben", 48000)

# Store as array to itterate through.
Employees = [emp1, emp2]

# Itterate through Employees array and run the show function.
for each in Employees:
    each.show()
