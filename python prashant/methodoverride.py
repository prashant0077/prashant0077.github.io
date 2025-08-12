# class Animal:
#     def sound(self,model, color):
#         print("Animal can Make Sound")
    
# class Dog(Animal):
#     def sound(self):
#         print("Dog can bark")


# an = Animal()
# dog = Dog()

# an.sound()

# dog.sound()



# class vehicle:
#     def price(self,model,color):
#         self.model 
#         self.color
#         print("vehicles are expensive")
# class car (vehicle, brand):
#     def price(self,brand):
#         self.brand
#         print("Car costs from rs 1000000 to 1000000000 ")
# class bike (vehicle,brand):
#         self.brand
#     def price(self, brand):
#         self.brand
#         print("bike costs from price 100000 to 10000000")
# class bus (vehicle,brand):
#         self.brand
#     def price(self):
#         print("bus cost from rs 3000000 to 300000000")
# veh = vehicle()
# car = car()
# bike = bike()
# bus = bus()


# veh.price()
# car.price()
# bike.price()
# bus.price()


class Vehicle:
    def __init__(self, model,color,price,name):

        self.model = model
        self.color =color
        self.price = price
        self.name = name
    
    def display(self):
        print("Name:",self.name)
        print("Model:",self.model)
        print("Price:", self.price)
        print("color:", self.color)

    def start(self):
        print("The Vehicle is starting by start button")
    

class Car(Vehicle):
    def start(self):
        print(f"The Car is starting by push button of{self.model} ")


class Bike(Vehicle):
    def start(self):
        print(f"The Bike is starting by kicking of {self.model} ")


car = Car("BA72","RED","10000000","Supra")
bike = Bike("PA400", "Green","1000000","Honda")

car.display()
print("-----------")
bike.display()

car.start()
bike.start()