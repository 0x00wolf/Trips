# TRIPS: A Dice-Game for Crips
#### video-url: <https://youtube.com/>
#### Description:
Trips is a dice gambling game that is very popular in Toronto, ON, Canada.

To begin a game every player places the agreed upon cash amount in the "pot". This earns
them the right to play in that round of Trips. Each player is given one dice to roll
when they put cash into the pot. The player with the lowest value gets to select who goes
first, and in the case of a tie would result in an immediate reroll among all the players
who tied. After the winner of the starting roll has determined who will roll first, players
take turns rolling. The goal is to have the lowest score at the end of the game, or to shoot
the moon (roll all 6's, which immediately ends the game regardless if there are players left
to roll).

**The game rules are simple:** Each player will roll 5 dice. The player is bound to keep
at least one of the rolls towards their final score. 3's are worth 0 points, all other
dice are worth their face value. The player may elect to keep all of the rolled dice, or reroll
the remaining dice after they have selected one to keep. This pattern will be repeated until
the player has selected 5 dice or run out of dice to roll. Players take turns in clockwise
order from the player selected to go first.

**Why build Trips?:** This game has nostalgic value for me. It also gave me the opportunity
to learn a fair bit about object oriented programming, which I did with the help of No Starch
Press's book: Object Oriented Python3. I also learned a fair bit about data organization
and list manipulation. Ultimately, the game is a lot more fun to play with actual dice, but
building it was a good learning experience for me and brought together a lot of different elements
of learning to code that I had absorbed over the last few months of my self education.

**How to run?**
Run python(3) ./tripsMain.py in the command line

**__File Breakdown:__**

**classplayer.py**
Creates the player class, which primarily holds variables required for the game. It imports
the dice class, and allows for a roll the dice function, relative to the remaining dice the player
has. It has another method to roll one dice for the player's roll for first. It also has an
update score roll, which loops through the player's dice kept and scores them (3's being 0 points,
and the rest of the dice being scored at face value).

**dice.py**
Imports random's randint function, and creates a class that is a range from 1, 6 and may be rolled
to produce a random value from that range.

**tripClass.py**
The trip class includes a number of variables and lists to store game players and player order. Also the player
up value, which is how the method's for the trip class will effectively create the game logic. The trip class
can also be seen as the game logic, where the tripMain.py (discussed next) can be seen as the game flow.

The methods in tripClass do the following:
1) Prompt for user input and returns the number of players for the game.
2) Add players' names and create instances of the player class for each.
3) Roll for first
4) A tiebreaker method incase more than one player ties for lowest roll.
5) The player who won the rolloff gets to select who goes first.
6) Displays the order in which players will roll.
7) Swaps the current player up variable for the next player up.
8) The current Player-up rolls the dice and selects which to keep.
9) A simple method to Displays the result of the roll.
10) A method to select which dice to keep.
11) Updates the players score by resetting score to zero and scoring all the dice with the
    method in the player class.
12) Displays the current player-up score.
13) Prompts the player-up to keep another dice from current rolls, keep all remaining
    rolled dice or reroll.
14) Checks to see if the player shot tbe moon, and if so exits the game, declaring them
    the winner.
15) Checks to see if the current player up won.
    or appends them to winners list if they tied for first.
16) This method declares a winner or resolves a tie if there are multiple players
    in the winners list.

**tripsMain.py**
This is the active file of the game and contains the game flow. It
encapsulates all the other classes and is condensed with no actual methods
or functions. The goal was to make as simple of a game logic to follow for trouble
shooting the far more complex game logic in tripClass.py.
