# OOP Object oriented programming

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"Машина {self.model} едет в {city}")

audi_car =  Car("Audi A6", 2020, "White")
Lada_car =  Car(color="Blue", model="Lada 2106", year=1999)

print(audi_car)
print(f"Model: {audi_car.model} Year: {audi_car.year} color: {audi_car.color}")
audi_car.color = "Yellow"
print(f"Model: {audi_car.model} Year: {audi_car.year} color: {audi_car.color}")