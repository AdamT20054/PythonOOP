# Encapsulation is a private variable or method within a class.
# Private variables or methods are only accessable within it's own class.

class Private:
    # Class Variables - All objects created by this class have the same variables
    purpose = "Show private variables within classes"

    # Constructor to initialize the object
    def __init__(self, name, note):
        # Instance variables passed through the function parameters.
        self.name = name # Public variable - can be called outside of the class.
        self.__note = note # Private variable - can only be called within it's own class.


    def show(self):
        print(self.name + " has the note: " + self.__note)
        
    def __private(self):
        print(self.__note)

Adam = Private("Adam", "Super secret note")


print(Adam.name) # Returns name because it is not private.

print(Adam.__private) # Retruns error because it is private.

print(Adam.__note) # Returns error:
# AttributeError: 'Private' object has no attribute 'note'
# Because __note is a private variable
# Private variables only accessable within its own class

