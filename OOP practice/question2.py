class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
class Car:
    def __init__(self,make,model,year,fuel_type,tank_capacity,fuel_level):
        super. __init__(make,model,year) 
        self.fuel_type = fuel_type
        self.tank_capacity = tank_capacity
        self.fuel_level = 0

    def refuel(self,amount):
        if self.fuel_level + amount <= self.tank_capacity:
            self.fuel_level += amount
            print(f"added {amount} litres of fuel. Current level: {self.fuel_level} litres")
        else:
            print(f"cannot add {amount} litres. tank capacity exceeded.")
            self.fuel_level = self.tank_capacity
            print(f"tank is full with {self.tank_capacity} litres.")

    def display_vehicle_info(self):
        print(f"make: {self.make}") 
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"fuel type: {self.fuel_type}")
        print(f"fuel level: {self.fuel_level}/{self.tank_capacity} litres")

#simulating driving
def drive(car,distance,fuel_consumption_per_km):
    fuel_needed = distance* fuel_consumption_per_km
    if car.fuel_level >= fuel_needed:
        car.fuel_level -= fuel_needed
        print(f"Driven {distance}km. Fuel used: {fuel_needed} litres. remaining fuel: {car.fuel_level} litres.")
    else:
        print(f"Not enough fuel to drive {distance}km .. refuel")

#create car object
my_car = Car("toyota", "prius", "2002", "petrol", 40, 23)

#simulating driving and refueling
my_car.display_vehicle_info()
drive(my_car, 100, 0.4)
my_car.refuel(40)
drive(my_car,100,0.4)
my_car.display_vehicle_info()
my_car.refuel(20)
                   
                

