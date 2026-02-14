class car():
    def __init__(self, name, color, power, price):
        self.name = name
        self.color = color
        self.power = power
        self.price = price
    def accelerate(self, amount):
        self.power += amount
        print(f"the car's power is {self.power} now.")

    def brake(self, amount):
        self.power -= amount
        if self.power < 0:
            self.power = 100
            print(f"the car's power is {self.power} now.")

nice_car = car("bugatti", "blue", 100, 2000000000)



nice_car.accelerate(235)
nice_car.brake(79)