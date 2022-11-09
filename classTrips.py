from classPlayer import *
from sys import exit
from time import sleep

class tripsGame():

    def __init__(self):
        self.numberOfPlayers = 0
        self.players = []
        self.playerUp = []
        self.rolls = []
        self.winningPlayer = Player('placeholder')
        self.winningPlayers = []
        self.playerWhoChooses = Player('placeholder')
        self.winningScore = 100

# prmpts for user input and returns the # of players for the game
    def getNumberOfPlayers(self):
        while True:
            number_of_players = input("Enter the number of players (2-15): ")
            try:
                number_of_players = int(number_of_players)
            except:
                print("The input must be a number between 2 and 15.")
                continue
            if number_of_players < 2 or number_of_players > 15:
                print("Please select a number of players between 2-15.")
                continue
            break
        self.numberOfPlayers = number_of_players

# Add players' names and create instances of the player class for each.
    def addPlayers(self):
        print()
        print("Input the names of the players in clockwise order.")
        while True:
            player_to_add = input("Input name of player: ")
            try:
                player_to_add = str(player_to_add)
            except:
                print("Player's name must be input as alphanumeric.")
                continue
            if player_to_add == '':
                print("Not providing a name makes for a bad game.\nTry again.")
                continue
            player_to_add = player_to_add.strip()
            player_to_add = Player(player_to_add)
            self.players.append(player_to_add)
            if len(self.players) == self.numberOfPlayers:
                break
        return self.players

# Roll for first
    def rollForFirst(self):
        rolls = []
        print()
        print('Rolling for first:')
        print()
        for player in self.players:
            sleep(.5)
            player.starting_roll = player.roll_first()
            print(f"{player.name.title()} rolled: {player.starting_roll}")
            rolls.append(player.starting_roll)
        lowest_value_rolled = min(rolls)
        contenders = []
        for player in self.players:
            if player.starting_roll == lowest_value_rolled:
                contenders.append(player)
        if len(contenders) > 1:
            print()
            print('Tie, rerolling players who tied')
            self.tieBreaker(contenders)
        else:
            player_who_chooses = contenders[0].name
            self.playerWhoChooses = player_who_chooses
            return self.playerWhoChooses

# Tiebreaker incase more than one player ties for lowest roll
    def tieBreaker(self, contenders):
        rolls = []
        print()
        for player in contenders:
            player.starting_roll = player.roll_first()
            print(f"{player.name.title()} rolled: {player.starting_roll}")
            rolls.append(player.starting_roll)
        print()
        lowestValueRolled = min(rolls)
        contendersCopy = contenders.copy()
        contenders = []
        for player in contendersCopy:
            if player.starting_roll == lowestValueRolled:
                contenders.append(player)
        if len(contenders) > 1:
            print()
            print('Tie!\nRerollin forg players who tied.')
            self.tieBreaker(contenders)
        else:
            self.playerWhoChooses = contenders[0].name
            return self.playerWhoChooses

# Player who won rolloff gets to select who goes first
    def selectFirstToRoll(self):
        print()
        while True:
            playerWhoRolls = input(f"{self.playerWhoChooses.title()}, "
                                + f"Select who rolls first (1-{len(self.players)}): ")
            for (i, player) in enumerate(self.players, start=1):
                print(i, player.name)
            try:
                playerWhoRolls = int(playerWhoRolls)
            except:
                print(f'Please select the player by the corresponding number (1-{self.numberOfPlayers})')
                continue
            playerWhoRolls = playerWhoRolls - 1
            break
        newOrder = []
        listA = self.players[playerWhoRolls:]
        listB = self.players[0:playerWhoRolls]
        for player in listA:
            newOrder.append(player)
        for player in listB:
            newOrder.append(player)
        self.players = newOrder

# Displays the order in which players will roll
    def displayFinalOrder(self):
        print("This is the final order:")
        print()
        for player in self.players:
            print(player.name.title())
            sleep(.5)

# Next player up
    def next_player_up(self):
        self.playerUp = self.players.pop(0)
        print()
        print(self.playerUp.name.title(), 'is next to roll')
        sleep(.5)

# Player-up rolls the dice and selects which to keep
    def rollTheDice(self):
        self.rolls = self.playerUp.roll_dice()
        self.selectDice()

# Displays tbe result of the roll
    def displayRolls(self):
        print(self.playerUp.name.title(), "rolled: ")
        sleep(1)
        for (i, roll) in enumerate(self.rolls, start=1):
            print("dice:", i, "roll:", roll)

# Function to select which dice to keep
    def selectDice(self):
        print()
        self.playerUp.remaining_dice = self.playerUp.remaining_dice - 1
        while True:
            self.displayRolls()
            playerKeeps = input(f"Select a dice to keep by its index # (1-{len(self.rolls)}): ")
            try:
                playerKeeps = int(playerKeeps)
            except:
                print("Select a dice by it's index number.")
                continue
            dice_rolled = len(self.rolls)
            if playerKeeps < 1 or playerKeeps > dice_rolled:
                print('You must select a dice corresponding to an available index number.')
                continue
            playerKeeps = playerKeeps - 1
            diceKept = self.rolls.pop(playerKeeps)
            self.playerUp.dice_kept.append(diceKept)
            self.playerUp.update_score(diceKept)
            break
        self.keepMoreOrRoll()

# Updates score by resetting score to zero and scoring all the dice in Player.dice_kept
    def updateScore(self):
        self.playerUp.score = 0
        for roll in self.playerUp.dice_kept:
            self.playerUp.update_score(roll)

# Displays the players score.
    def display_score(self):
        print('Player:', self.playerUp.name.title(), 'Rolls kept:', self.playerUp.dice_kept, 'Current score:', self.playerUp.score)

# Prompts player to keep another dice from current rolls, keep all remaining rolled dice or reroll
    def keepMoreOrRoll(self):
        print()
        if self.playerUp.remaining_dice != 0:
            print(f'Dice kept: {self.playerUp.dice_kept}')
            keepMore = input(f"{self.playerUp.name.title()}, make your selection:\n"
                + "     'y' to select another die to keep from the dice.\n"
                + "     'k' to add all of the current rolls to your score.\n"
                + "     'r' to reroll the remaining dice.\n")
            if keepMore == 'y':
                print()
                self.selectDice()
            elif keepMore == 'k':
                for roll in self.rolls:
                    self.playerUp.dice_kept.append(roll)
                self.playerUp.remaining_dice = 0
                print()
            else:
                return
        else:
            print()

# Checks to see if the player shot tbe moon, and if so exits the game
    def check_shot_the_moon(self):
        if self.playerUp.score == 30:
            print()
            print(self.playerUp.name.title(), 'shot the moon and won!')
            exit()

# Checks to see if the current player up won,
# or appends them to winners list if they tied for first.
    def check_winner(self):
        if self.playerUp.score < self.winningScore:
                self.winningScore = self.playerUp.score
                self.winningPlayer = self.playerUp
                self.winningPlayers = []
                self.winningPlayers.append(self.playerUp)
                print()
                print(self.winningPlayer.name.title(), "you are currently winning.")
                sleep(.5)
        elif self.playerUp.score == self.winningPlayer.score:
            self.winningPlayers.append(self.playerUp)
            print()
            print(self.playerUp.name.title(), "has tied for first.")
        else:
            print()
            print("Sorry, you are out!")

# Declares a winner or resolves a tie if there are multiple players
# in the winners list.
    def declare_winner_or_resolve_tie(self):
        if len(self.winningPlayers) != 1:
            for player in self.winningPlayers:
                playerInTiebreaker = self.winningPlayers.pop(0)
                self.players.append(playerInTiebreaker)
                print(f'{player.name.title()} is in the tiebreaker!')
            self.gameFlow()
        elif len(self.winningPlayers) == 1:
            print()
            print(self.winningPlayer.name.title(), 'Wins!!!')
        else:
            print('broken')