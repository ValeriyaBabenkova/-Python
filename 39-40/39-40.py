# Задача 1
def conversion (rub, course):
    return (f'За {rub} рублей вы получите {rub*course} долларов ')

print (conversion(1000, 0.0111331))

# Задача 2

def age (userAge):
    return userAge>18

print(age(int(input('Введите ваш возраст:'))))

