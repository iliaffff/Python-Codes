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
while True:
    print("\n\t\t\tMain Menu\n")
    print("\t1.Show Fares")
    print("\t2.Rent a Car")
    print("\t3.Exit\n")

    userChoice = int(input("Please Enter Your Choice: "))
    if userChoice == 1:
        car.showCarFare()
    elif userChoice == 2:
        carType = input("Which type of car you want to rent? ")
        dayOfUse = int(input("How many days you want to rent? "))
        print(f"The cost is ${car.calculateFare(carType, dayOfUse)}")
    elif userChoice == 3:
        break


        

