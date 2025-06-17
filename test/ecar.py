from car import Car

class ElectricCar(Car):
        def __init__(self, brand, model, battery_capacity):
        # Initialize the base class with fuel_type as 'Electric'
            super().__init__(brand, model, fuel_type="Electric")
            self.battery_capacity = battery_capacity

        def charge_battery(self):
            print(f"{self.brand} {self.model} is charging. Battery capacity: {self.battery_capacity} kWh.")

    # Method overriding: redefining start_engine to customize for electric cars
        def start_engine(self):
        # This overrides the parent class's start_engine method
            print(f"{self.brand} {self.model} powers on silently. (Electric Start)")

my_electric_car = ElectricCar("Tesla", "Model 3", 75)
my_electric_car.start_engine()     # Uses overridden method in ElectricCar
my_electric_car.charge_battery()
my_electric_car.stop_engine()      # Inherited from Car (not overridden)