class Car:
    def __init__(self, plate, model, color, horsepower):
        self.plate = plate
        self.model = model
        self.color = color
        self.horsepower = horsepower

    def __str__(self):
        return f'{self.plate} {self.model} {self.color} {self.horsepower}'

    def utilization_fee(self):
        return 114500 + (self.horsepower * 100)

    def transport_tax(self):
        return self.horsepower * 35