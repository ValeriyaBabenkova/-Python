
class Shop:
    PRODUCTS = {'молоко' : 10, 'колбаса': 20}
    productsForSale = ['яйца', 'колбаса']
    def __init__(self):
        self.count = 0
        self.all_sum = 0
    def buy(self, name):
        """Покупка продуктов"""
        name = name.lower()
        if name in self.productsForSale and name in self.PRODUCTS:
            self._check_discount(name)
        if name in self.PRODUCTS :
            self.all_sum += self.PRODUCTS[name]
            self.count += 1
            print(f'Купили "{name}"')
        else:
            print(f'Продукта "{name}" нет в базе')

    def _check_discount(self, name):
        print(f'Прошла скидка на товар "{name}"')
        self.PRODUCTS[name] -= 5


    def add_product(self, name, price):
        """Добавляем продукт в базу"""
        self.PRODUCTS[name] = price
        print(f'Добавили в базу "{name}"')

    def get_info(self):
        print(f'Всего купили на {self.all_sum}р.')
        print(f'Всего чеков {self.count}')
        print('Хорошего дня!')

    def delete_product(self, name):
        name = name.lower()
        self.PRODUCTS.pop(name)
        print(f'Удалили из базы "{name}"')

shop = Shop()
shop.buy('Молоко')
shop.buy('Яйца')
shop.buy('Колбаса')
shop.add_product('яйца', 100)
shop.buy('Яйца')
shop.delete_product('Молоко')
shop.buy('Молоко')
shop.get_info()

