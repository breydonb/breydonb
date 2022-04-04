import string


class PolymorphicCar:

    make = ""
    model= ""
    year = 0

    ## __init__ acts like our constructor

    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def getMake(self) -> string:
        return self.make

    @property
    def getModel(self) -> string:
        return self.model

    @property
    def getYear(self) -> int:
        return self.year

class Toyota(PolymorphicCar):
    def getHorsePower(self) -> float:
        return 172.5
    