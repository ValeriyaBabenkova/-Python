
class Shop:
    def __init__(self):
        self.products = {'яблоко': 200, 'манго': 100}
        self.check = 0
    def buy_prouduct(self, name):
        if name not in self.products:
            raise ValueError('Такого товара нет')
        self.check += self.products[name]
        print(f'Купили товар {name}')
    def add_product(self, name, price):
        if price < 0:
            raise ValueError('Цена должна быть положительной')
        if len(name) < 3:
            raise ValueError('В названии товара должно быть больше трёх букв')
        self.products.update({name: price})
        print(f'Добавили товар {name} по цене {price}')

shop = Shop()
while True:
    print('Что вы хотите сделать: ')
    print('1 - купить товар')
    print('2 - добавить товар')
    ans = input('Выберите: ')
    try:
        if ans == '1':
            name = input('Введите название товара: ')
            shop.buy_prouduct(name)
        elif ans == '2':
            name = input('Введите название товара: ')
            price = int(input('Введите цену товара: '))
            shop.add_product(name, price)
    except ValueError as e:
        print(e)