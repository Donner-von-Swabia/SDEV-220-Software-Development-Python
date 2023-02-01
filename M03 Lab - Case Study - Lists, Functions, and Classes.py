class Vehicle:
    def __init__(self,type):
        self.type = type

class Automobile:
    def __init__(self,year,make,model,doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.door = doors
        self.roof = roof

car = Vehicle(str(input("Enter the type of vehicle : ")))
auto = Automobile(int(input("Enter the year on the vehicle : ")),str(input("Enter the make of the vehicle : "))
    ,str(input("Enter the model of the vehicle : ")),int(input("How many doors does the vehicle have :"))
    ,str(input("Enter the type of roof of the vehicle :"))
)

print("Vehicle type:" ,car.type)
print("Year :", auto.year)
print("Make :", auto.make)
print("Model :", auto.model)
print("Number of Doors :", auto.door)
print("Type of roof: ", auto.roof)
