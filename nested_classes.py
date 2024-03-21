class Car:
    def __init__(self):
        self.cars = []

    def addCar(self, brand, model):
        sportsCar = self.SportsCar(brand, model)
        self.cars.append(sportsCar)

    class SportsCar:
        pass

        def __init__(self, brand, model):
            super().__init__()
            self.brand = brand
            self.model = model

        def printAll(self):
            print(f"Brand: {self.brand}, Model: {self.model}")

myCar = Car()
myCar.addCar("Tesla", "Refreshed Model 3")
myCar.addCar("Porsche", "911 GT3 RS")
myCar.addCar("Mercedes Benz", "AMG GT")
myCar.addCar("Rivian", "R1S")

for car in myCar.cars:
    car.printAll()