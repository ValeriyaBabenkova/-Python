
class Programmer:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.hours = 0
        self.money = 0
        self.money_info = {'Junior': 10, 'Middle': 15, 'Senior': 20}


    def work(self, time):
        if self.grade == 'Junior':
            self.hours += time
            money = self.money_info['Junior']
            self.money += time*money
        if self.grade == 'Middle':
            self.hours += time
            money = self.money_info['Middle']
            self.money += time * money
        if self.grade == 'Senior':
            self.hours += time
            money = self.money_info['Senior']
            self.money += time * money


    def rise(self):
        if self.grade == 'Junior':
            self.grade = self.grade.replace('Junior', 'Middle')
        elif self.grade == 'Middle':
            self.grade = self.grade.replace('Middle', 'Senior')
        else:
            self.money_info['Senior'] += 1



    def info(self):
        print(f'{self.name} {self.hours} {self.money}тгр.')



programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
