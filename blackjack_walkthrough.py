from p1_random import P1Random # Imports the input from other file

rng = P1Random() # outside of the loop

# print(rng.next_int(13) + 1)

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0

# Control the number of games the player will play
while game_continue: # game #1, #2, #3
    # 1. print game number message
    game_num += 1
    print(f"START GAME #{game_num}")
    # 2. deal a card to the player automatically
    player_hand = 0
    # deal a card to the player
    card = rng.next_int(13) + 1 # [0, 12] + 1 => [1, 13]
    if card == 1:
        print("Ace")
        card = 1
    elif 2 <= card <= 10:
        # print out the card value
        print(card)
    elif card == 11:
        print("Jack")
        card = 10
    elif card == 12:
        print("Queen")
        card = 10
    elif card == 13:
        print("King")
        card = 10
    # 3. add card number to the player hand value
    # 4. print hand value
    # Keep playing the current game by prompting the player to choose a menu option
    no_winner = True
    while no_winner:
        # print four menu options
        # ask/prompt player for an input to choose a menu option
        option = int(input("Some message"))
        if option ==1:
            # deal another card to the player
            # calculate the player's hand value
            # if player_hand == 21, print winning message
            # elif player_hand > 21, print losing message
            # update the number of games player/dealer wins
            # set no_winner = False
            pass # want to go back here to look at implementation details by yourself
        elif option == 2:
            # deal a card to the dealer
            dealer_hand = rng.next_int(11) + 16 # a random number in range [16, 26]
            # compare player hand with dealer hand value
            # and determine who wins the game
            # update number of games player/dealer wins
            # set no_winner = False
            pass
        elif option == 3:
            #print stats: player_wins and dealer_wins
            pass
        elif option ==4:
            no_winner = False # get outside of the inner while
            game_continue = False # get outside of outer whi;e
        else:
            # print invalid message