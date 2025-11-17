class Residence:
    def __init__(self, city, street, house, flat):
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return f'{self.city} {self.street} {self.house} {self.flat}'