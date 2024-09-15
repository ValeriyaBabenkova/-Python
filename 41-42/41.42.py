class Car:
    def __init__(self, color,fuel, consumption, kmage=0):
        self.color = color
        self.fuel = fuel
        self.consumption = consumption
        self.kmage = kmage
        print(f'{self.color} {self.fuel}')


    def drive(self, km):
        need_fuel = (km * self.consumption) / 100
        if need_fuel <= self.fuel:
            print(f'Вы проехали {km} км')
            self.fuel -= need_fuel
            self.kmage += km
            print(f'У вас осталось {self.fuel} л топлива')
        else:
            print('Вам не хватит топлива')


    def get_mileage(self):
        return print(self.kmage)

car = Car(color = 'синий', fuel = 20, consumption = 7)

car.drive(280)
car.get_mileage()
