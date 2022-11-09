from classDice import *

class Player():
    def __init__(self, name):
        self.name = name
        self.remaining_dice = 5
        self.d6 = Dice()
        self.score = 0
        self.dice_kept = []
        self.starting_roll = 0
        self.winning = False

    def roll_first(self):
        self.starting_roll = self.d6.roll()
        return self.starting_roll

    def roll_dice(self):
        dice_rolled = [self.d6.roll() for v in range(0, self.remaining_dice)]
        return dice_rolled

    def update_score(self, dice_roll):
        if dice_roll == 3:
            self.score = self.score
        else:
            self.score = self.score + dice_roll