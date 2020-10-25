import random
import sys

class Die:
    def __init__(self,n=6):
        self.sides  = n
        self.roll()

    def roll(self):
        self.face   = int(random.random()*self.sides+1)

class Player:
    def __init__(self, title):
        self.name   = title
        self.score  = 0
        self.die    = Die(6)

    def move(self):
        self.player_turn()

    def player_turn(self):
        turn_total  = 0
        replay      = 'r'
        while replay == 'r' or replay == 'h':
            if replay == 'r':
                self.die.roll()
                roll = self.die.face
                if roll == 1:
                    print('{} rolled a 1'.format(self.name))
                    turn_total = 0
                    replay = 'n'
                else:
                    print('{} rolled a {}'.format(self.name, roll))
                    turn_total = turn_total+roll
                    print('{}\'s turn total is {}'.format(self.name, turn_total))
                    replay = raw_input('what action? (r/h) ')
            elif replay == 'h':
                self.score += turn_total
                print('\n{}\'s turn total was added to player score.'.format(self.name))
                replay = 'n'
        print('{}\'s turn is over'.format(self.name))
        print('{}\'s total score is {}\n'.format(self.name, self.score))

    def machine_turn(self):
        turn_total  = 0
        replay      = 'r'
        while replay == 'r' or replay == 'h':
            if replay == 'r':
                self.die.roll()
                roll = self.die.face
                if roll == 1:
                    print('{} rolled a 1'.format(self.name))
                    turn_total = 0
                    replay = 'n'
                else:
                    print('{} rolled a {}'.format(self.name, roll))
                    turn_total = turn_total+roll
                    print('{}\'s turn total is {}'.format(self.name, turn_total))
                    if turn_total > 25 and turn_total < (100 - turn_total):
                        replay = 'h'
                    else:
                        print('Machine rolls again')
            elif replay == 'h':
                self.score += turn_total
                print('\n{}\'s turn total was added to player score.'.format(self.name))
                replay = 'n'
        print('{}\'s turn is over'.format(self.name))
        print('{}\'s total score is {}\n'.format(self.name, self.score))

class Pig:
    def __init__(self):
        self.die    = Die()
        self.p1     = Player('Player 1')
        self.p2     = Player('Computer')

    def play(self):
        while self.p1.score < 100 and self.p2.score < 100:
            self.p1.move()
            if self.p1.score < 100:
                self.p2.machine_turn()
        if self.p1.score > self.p2.score:
            print('Player 1 Wins')
            sys.exit()
        else:
            print('Computer Wins')
            sys.exit()

def main():
    random.seed(0)
    game = Pig()
    game.play()

main()
