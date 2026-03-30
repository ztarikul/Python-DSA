class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive! ", self.brand)
    

class Boat:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!", self.brand)

class Plane:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!", self.brand)



car1 = Car("Ford", "Sedan")
boat1 = Boat("Yamaha", "cruse")
plane1= Plane("Boeing", "747")

for x in (car1, boat1, plane1):

    x.move()