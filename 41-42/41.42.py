import random
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
        else:
            print('Вам не хватит топлива')


    def get_mileage(self):
        return print(self.kmage)

class SportCar(Car):
    def fast_drive(self, km):
        need_fuel = (km * self.consumption*1.5) / 100
        if need_fuel <= self.fuel:
            print(f'Вы проехали {km} км')
            self.fuel -= need_fuel
            self.kmage += km
        else:
            print('Вам не хватит топлива, чтобы доехать до места')

    def competition(self):
        if random.randint(0, 1) == 0:
            print('Ваша машина победила!!!')
        else:
            print('К сожалению, вы проиграли...')

# car = Car(color = 'синий', fuel = 20, consumption = 7)
#
# car.drive(280)
# car.get_mileage()

car1 = Car(color='черный', fuel=8, consumption=8,kmage=0)
car2 = SportCar(color='черный', fuel=8,consumption=8, kmage=0)

print('\nПервая машина')
for i in range(4):
    car1.drive(30)


print('\nВторая машина')
for i in range(4):
    car2.fast_drive(30)

print(car2.competition())
