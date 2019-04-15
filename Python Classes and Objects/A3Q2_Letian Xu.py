# Letian Xu
# 02-16-2019
# I have not given or received any unauthorized assistance on this assignment.

'''
This is a gamble game, the player will use the cup class to roll closer score for game goal.
After rolling, the original balance will updated based on corresponding rules. 
Until the player's balance become 0, the game can keep going on.
Notes: you will need to type yes to get into next step in this game;
    you will have to type a number as your bet, and should not be negative number or text,
    if the bet you type in was over your current balance, 
    the game will remind you and let you type another bet number.
'''

import random
from random import randint

class SixSidedDie:
    def __init__(self):
        self.value = 0
    
    def roll(self):
        self.value = randint(1,6)
        return self.value

    def getFaceValue(self):
        return self.value

    def __repr__(self):
        return 'SixSidedDie(%d)'%(self.value)

class TenSidedDie(SixSidedDie):
    def roll(self):
        self.value = randint(1,10)
        return self.value

    def __repr__(self):
        return 'TenSidedDie(%d)'%(self.value)

class TwentySidedDie(SixSidedDie):
    def roll(self):
        self.value = randint(1,20)
        return self.value

    def __repr__(self):
        return 'TwentySidedDie(%d)'%(self.value)

class Cup:
    def __init__(self, six = 1, ten = 1, twenty =1):
        self.total = 0
        self.dice = []
        for _ in range(0, six):
            self.dice.append(SixSidedDie())
        for _ in range(0, ten):
            self.dice.append(TenSidedDie())
        for _ in range(0, twenty):
            self.dice.append(TwentySidedDie())

    def roll(self):
        self.total = 0
        for _ in self.dice:
            self.total += _.roll()
        return self.total

    def getSum(self):
        return self.total
    
    def __repr__(self):
        return'Cup(' +','.join([str(d) for d in self.dice]) + ')'

# used to check the bet
def check_bet(num,balance):
    try:
        num = int(num)
        if num < 0:
            return False
        else:
            if num > balance:
                print("You don't have enough money!")
                return False 
            else:
                return True
    except:
        return False


def main():
    print('Welcome!')
    user_name = input("Enter your name: ")
    balance = 100

    game_start = input("Would you like to play this game?")
    if game_start.lower() != 'yes':
        print('Goodbye!')
        return None
    
    while True:
        game_goal = randint(1,100)
        print("The Goal of this game is", game_goal)

        while True :
            bet = input("How much you want to bet?")
            res = check_bet(bet,balance)
            if res:
                break
            
        bet = int(bet)           
        balance -= bet
        six, ten, twenty = input("How many of each die they would like to roll?(format:six ten twenty)").split(' ')
        
        print("Let's rolling!")
        c = Cup(int(six), int(ten), int(twenty))
        print("Your score is:", c.roll())
        result = c.getSum()
        
        if result == game_goal:
            balance += 10*bet
        elif result >= game_goal - 5 and result < game_goal:
            balance += 5*bet
        elif result >= game_goal - 10 and result < game_goal - 5:
            balance += 2*bet

        print(user_name, balance)
        play_again = input("Would you like to play again? ")
        if play_again.lower() !='yes':
            print('Goodbye!')
            return None
        # when player's balance equal to 0, the game was over.
        elif balance <= 0:
            print("You‘re broke!")
            return None

if __name__ == '__main__':
    main()