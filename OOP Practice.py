class CarTypeNotFoundError(Exception):
    pass

class Car:
    def __init__(self):
        self.carFare = {"Hatchback": "$30", "Sedan": "$50", "SUV": "$100"}

    def showCarFare(self):
        print("Cost per day:")
        print("Hatchback - $30")
        print("Sedan - $50")
        print("SUV - $100")

    def calculateFare(self, carType, daysOfUse):
        if carType not in self.carFare.keys():
            raise CarTypeNotFoundError
        price = int(self.carFare[carType].strip("$"))
        result = price * daysOfUse
        return result
    
car = Car()

        

