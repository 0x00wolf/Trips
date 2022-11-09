from classTrips import *
import sys

while True:
    print('\n'*6)
    print('Welcome to ***Trips***')
    print()
    print("Input 'p' to play,")
    print("or 'r' to display the rules.")
    print("or 'q' to quit.")
    print()
    user_input = input('Make selection: ')
    print()
    if user_input == 'p':
        while True:
            oGame = tripsGame()
            oGame.getNumberOfPlayers()
            oGame.addPlayers()
            oGame.rollForFirst()
            oGame.selectFirstToRoll()
            oGame.displayFinalOrder()
            while len(oGame.players) != 0:
                        oGame.next_player_up()
                        while len(oGame.playerUp.dice_kept) < 5:
                            oGame.rollTheDice()
                            oGame.updateScore()
                            oGame.display_score()
                        oGame.check_shot_the_moon()
                        oGame.check_winner()
            oGame.declare_winner_or_resolve_tie()
            print()
            print('Play again?')
            play_again = input("Input 'y' to play again\n'q' to quit: ")
            if play_again == 'y':
                continue
            else:
                sys.exit()
    elif user_input == 'r':
        filename = 'tripsRules.txt'
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
        print()
        done = input('Finished? Press enter.')
        continue
    else:
        sys.exit()
