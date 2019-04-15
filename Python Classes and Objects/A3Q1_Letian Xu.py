# Letian Xu
# 02-16-2019
# I have not given or received any unauthorized assistance on this assignment.

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