class Vehicle:
    class_attribute = "Afto einai ena oxima"

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def displayInfo(self):
        print(f"Name: {self.name}, Color: {self.color}")

    @classmethod
    def classMethod(cls):
        print("This is a class method")
        print(f"We can have access to the class attribute {cls.class_attribute}")

    #static method
    @staticmethod
    def staticMethod():
        #it doesnt have access to the class or to the instance attributes
        print("I am a static method. I dont have access to anything!")

#subclass/child class
class Car(Vehicle):
    #subclass/child constructor
    def __init__(self, name, color, fuel_type):
        #using super function to invoke init method of the supercell/parent class so that we can access name and color attributes
        super().__init__(name, color)
        #ftiaxnoume kai to attribute gia to fuel type
        self.fuel_type = fuel_type

    #subclass overriding the display info method
    def displayInfo(self):
        print(f"Name: {self.name}, Color: {self.color}, Fuel Type: {self.fuel_type}")

#creating object of the parent class
vehicle = Vehicle("AMG", "Black")
#invoking instance method
vehicle.displayInfo()
#creating object of subclass/child
car = Car("Mercedes", "Silver", "Diesel")
#invoking overriden method
car.displayInfo()
print(Vehicle.class_attribute)

#invoking static method
Vehicle.staticMethod()