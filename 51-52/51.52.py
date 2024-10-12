import random
class Player:
    def __init__(self, name, wins=0):
        self.name = name
        self.wins = wins
    def __str__(self):
        return self.name

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.wins1 = 0
        self.wins2 = 0
    def get_cubes(self):
        return random.randint(1,6)+random.randint(1,6)
    def play_round(self):
        self.result_player1 = self.get_cubes()
        print(f'{player1} выбросил {self.result_player1}')
        self.result_player2 = self.get_cubes()
        print(f'{self.player2} выбросил {self.result_player2}')

        if self.result_player1 > self.result_player2:
            self.wins1 += 1
            print(f'Победил {self.player1}')

        elif self.result_player1 < self.result_player2:
            self.wins2 += 1
            print(f'Победил {self.player2}')
        else:
            print('Ничья')


    def get_statistic(self):
        print(f'{self.player1} победил {self.wins1}\n{self.player2} победил {self.wins2}' )


player1 = Player("Dima")
player2 = Player("Alex")

game = Game(player1, player2)
# game = Game('Ben', 'Tom')

game.play_round()
game.play_round()
game.play_round()

game.get_statistic()