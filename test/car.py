class Car:
    def __init__(self,brand,model,fuel_type):
        self.brand=brand
        self.model=model
        self.fuel_type=fuel_type

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started using {self.fuel_type}")

    def stop_engine(self):
        print(f"{self.brand} {self.model}'s engine stopped.")

my_car = Car("Audi", "A6", "Petrol")
my_car.start_engine()       
my_car.stop_engine()
