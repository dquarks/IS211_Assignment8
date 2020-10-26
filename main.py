import random
import sys
import time
import argparse

class Die:
    def __init__(self,n=6):
        self.sides  = n
        self.roll()

    def roll(self):
        self.face   = int(random.random()*self.sides+1)

class Player:
    def __init__(self, title,human_player=False):
        self.name   = title
        self.human  = human_player
        self.score  = 0
        self.die    = Die(6)

    def move(self):
        if self.human:
            self.player_turn()
        else:
            self.machine_turn()

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
    def __init__(self, p1_name, p2_name, p1_human=True, p2_human=False):
        self.die    = Die()
        self.p1     = Player(p1_name,p1_human)
        self.p2     = Player(p2_name,p2_human)

    def play(self):
        while self.p1.score < 100 and self.p2.score < 100:
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()
        if self.p1.score > self.p2.score:
            print('{} Wins'.format(self.p1.name))
            sys.exit()
        else:
            print('{} Wins'.format(self.p2.name))
            sys.exit()

class TimedPigProxy:
    def __init__(self, p1_name, p2_name, p1_human=True, p2_human=True):
        self.die    = Die()
        self.timer  = time.time()
        self.tend   = self.timer + 60
        self.p1     = Player(p1_name,p1_human)
        self.p2     = Player(p2_name,p2_human)

    def play(self):
        while (self.p1.score < 100 and self.p2.score < 100) and (time.time() < self.tend):
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()
        if(time.time() > self.tend):
            print('Time is up!')
        if self.p1.score > self.p2.score:
            print('{} Wins'.format(self.p1.name))
            sys.exit()
        else:
            print('{} Wins'.format(self.p2.name))
            sys.exit()

class PlayerFactory:
    def __init__(self,p1_type, p2_type):
        self.player1_type = p1_type
        self.player2_type = p2_type

    def start_normal(self):
        p1_tag = 'Player 1'
        p2_tag = 'Player 2'
        if self.player1_type == False:
            p1_tag = 'Computer 1'
        if self.player2_type == False:
            p2_tag = 'Computer 2'
        random.seed(0)
        game = Pig(p1_tag, p2_tag, self.player1_type, self.player2_type)
        game.play()

    def start_timed(self):
        p1_tag = 'Player 1'
        p2_tag = 'Player 2'
        if self.player1_type == False:
            p1_tag = 'Computer 1'
        if self.player2_type == False:
            p2_tag = 'Computer 2'
        random.seed(0)
        game = TimedPigProxy(p1_tag, p2_tag, self.player1_type, self.player2_type)
        game.play()

def main(type1, type2, game_type=False):
    print('Working: {} {}'.format(str(type1), str(type2)))
    val1 = -1
    val2 = -1
    if(type1.lower() == 'human'):
        val1 = True
    elif(type1.lower() == 'computer'):
        val1 = False
    else:
        print('Error unknown player 1 type!')
# ----->
    if(type2.lower() == "human"):
        val2 = True
    elif(type2.lower() == "computer"):
        val2 = False
    else:
        print('Error unknown player 2 type!')

    if(val1 != -1 and val2 != -1):
        players = PlayerFactory(val1, val2)
        if(game_type == False):
            players.start_normal()
        else:
            print('Playing timed')
            players.start_timed()

if len(sys.argv) <= 2:
    exit()
parser = argparse.ArgumentParser()
parser.add_argument('--player1', help='Enter Playe 1 Type: human or computer')
parser.add_argument('--player2', help='Enter Playe 2 Type: human or computer')
parser.add_argument('--timed', help='Toggle timed game mode',action='store_true')
arg = parser.parse_args()

try:
    main(arg.player1,arg.player2,arg.timed)
except Exception as exception:
    print(str(exception))
