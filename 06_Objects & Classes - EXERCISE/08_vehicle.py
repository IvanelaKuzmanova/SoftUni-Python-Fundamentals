class Vehicle:

    def __init__(self, type, model, price, owner = None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner == None:
            result = f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
            self.owner = owner
        elif money < self.price:
            result = "Sorry, not enough money"
        elif self.owner != None:
            result = "Car already sold"

        return result

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            result = f"{self.model} {self.type} is on sale: {self.price}"

        return result


#-------------Tets code-------------

# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
