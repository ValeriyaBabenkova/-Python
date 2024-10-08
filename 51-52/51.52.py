import random
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        # print(self.name)
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def play_round(self):
        result_player1 = random.randint(1,6)+random.randint(1,6)
        print(f'{player1}выбросил {result_player1}')
        result_player2 = random.randint(1,6)+random.randint(1,6)
        print(f'{self.player2}выбросил {result_player2}')

        if result_player1 > result_player2:
            print(f'Победил {self.player1}')
        elif result_player1 < result_player2:
            print(f'Победил {self.player2}')
        else:
            print('Ничья')


player1 = Player("Dima")
player2 = Player("Alex")

game = Game(player1, player2)
# game = Game('Ben', 'Tom')

game.play_round()
game.play_round()