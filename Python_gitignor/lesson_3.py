class MusicPlayable:
    @staticmethod
    def play_music(song):
        print(f"играет музыка {song}...")

class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
       return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
    print("Машина едет...")

    def__str__(self):
    return f"MOdel: {self.__model} Year: {self.__year}"

class ElectricCar(Car):
    def __init(self, model, year, bettery):
        Car.__init__(self, model, year)
        self.__betery = bettery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__betery = value

    def drive(self):
        print(f"Машина  {self.model}  едет на электричестве...")

class FuelCar(Car):
__total_fuel = 5000

    @staticmethod
    def Fuel_type():
        print("AI - 95")

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

