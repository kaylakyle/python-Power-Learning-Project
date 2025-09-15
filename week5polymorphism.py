class Car:
    def move(self):
        print("Driving ")

class Plane:
    def move(self):
        print("Flying ")

class Boat:
    def move(self):
        print("Sailing ")

# Polymorphism 
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Same method name, different behavior
