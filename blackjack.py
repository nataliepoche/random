from p1_random import P1Random # Imorts the random list of numbers

rng = P1Random()

# defined values inside of loop
user_input = 1 # sets the consition of the game
game = 1 # Starts keeping track of the rounds
player_hand = 0 # Starts keeping track of player hand
player_wins = 0 # Starts keeping track of player wins
dealer_wins = 0 # Starts keeping track of dealer_wins
dealer_hand = 0 # Keeps track of the dealer's hand
tie = 0 # Counts toes
card_value = 0 # value of the card

while user_input != 4: # Makes sure that 4 exists the game
    # Start by drawing the random card
    print(f"START GAME #{game}")

    # Draw another random card and go through the scenarios again
    card_name = rng.next_int(13) + 1  # Draws a random card, the + 1 includes 0 and 13 as possible numbers

    # Transorm the card into values decides the "Your card is a"
    card_value = 0  # sets the card value
    if card_name == 13:
        print("Your card is a KING!")  # States the card as a king
        card_value = 10  # sets the value of the King as 10
    elif card_name == 12:
        print("Your card is a QUEEN!")  # States the card as a queen
        card_value = 10  # states the value of a queen as 10
    elif card_name == 11:
        print("Your card is a JACK!")  # States the card as a jack
        card_value = 10  # States the value of jack as 10
    elif card_name == 1:
        print("Your card is a ACE!")  # States the card as Ace
        card_value = 1  # States the value of ace is 1
    elif card_name >= 1 and card_name <= 10:
        print(f"Your card is a {card_name}!")  # States the card
        card_value = card_name  # States the value of card is the same as the name
    player_hand += card_value
    print(f"Your hand is: {player_hand}")  # States the total value of what you have

    game += 1 # Adds another game when starting to keep track of rounds

    current_game = True # Creates a new loop

    while current_game == True: # Sets up options to game
        # Print list of options
        print("1. Get another card \n2. Hold hand \n3. Print statistics \n4. Exit")


        user_input = int(input("Choose an option: ")) # Allows player to choose from options
        # Execute Options
        if user_input == 1:

            # Draw another random card and go through the scenarios again
            card_name = rng.next_int(13) + 1  # Draws a random card, the + 1 includes 0 and 13 as possible numbers

            # Transorm the card into values decides the "Your card is a"
            if card_name == 13:
                print("Your card is a KING!")  # States the card as a king
                card_value = 10  # sets the value of the King as 10
            elif card_name == 12:
                print("Your card is a QUEEN!")  # States the card as a queen
                card_value = 10  # states the value of a queen as 10
            elif card_name == 11:
                print("Your card is a JACK!")  # States the card as a jack
                card_value = 10  # States the value of jack as 10
            elif card_name == 1:
                print("Your card is a ACE!")  # States the card as Ace
                card_value = 1  # States the value of ace is 1
            elif card_name >= 1 and card_name <= 10:
                print(f"Your card is a {card_name}!")  # States the card
                card_value = card_name  # States the value of card is the same as the name
            player_hand += card_value
            print(f"Your hand is: {player_hand}") # States the total value of what you have

            # Ensure the value isn't over 21
            if player_hand > 21:
                print("You exceeded 21! You lose.") # States the dealer wins
                dealer_wins += 1 # Adds up dealer wins
                player_hand = 0 # Resets player's hand
                current_game = False # Ends the round

            # if it is 21 stop and player wins
            if player_hand == 21:
                print("BLACKJACK! You win!") # States the player wins
                player_wins += 1 # Adds up player wins
                player_hand = 0 # Resets player's hand
                current_game = False # Ends the round

        elif user_input == 2: # Hold hand
            # dealer's card
            card_name = rng.next_int(11) + 16  # Draws a random card, the + 1 includes 0 and 13 as possible numbers for the dealer's hand
            print(f"Dealer's hand: {card_name}") # Gives the dealer's hand
            print(f"Your hand is: {player_hand}") # Player's current cards

            if card_name > 21:
                print("You win!") # States you win if you go over 21 at some point
                player_wins += 1 # Adds when the player wins
                player_hand = 0 # Resets the player's hand for another game
                current_game = False # Ends the current game
            elif card_name == player_hand: # Creates a tie when the dealer's hand and player's hand are the same
                print("It's a tie! No one wins!") # States that it's a tie
                tie += 1 # Counts the number of ties
                player_hand = 0 # Resets the player's hand
                current_game = False # Ends the current game
            elif card_name > player_hand: # When dealer is higher than player, dealer wins
                print("Dealer wins!") # States dealer wins
                dealer_wins += 1 # Counts deler wins
                player_hand = 0 # Resets player's hand
                current_game = False # Ends the current game
            elif card_name < player_hand: # If dealer's hand is less than player, than player wins
                print("You win!") # States player wins
                player_wins += 1 # Adds player wins
                player_hand = 0 # Resets player's hand
                current_game = False # Ends current game
        elif user_input == 3: # Statistics
            total = player_wins + dealer_wins + tie # Finds the total games
            percentage = (player_wins / total) * 100 # Finds percentage of player wins
            print(f"Number of Player wins: {player_wins}") # Prints player wins
            print(f"Number of Dealer wins: {dealer_wins}") # Prints dealer wins
            print(f"Number of tie games: {tie}") # Prints ties
            print(f"Total # of games played is: {total}") # Prints total games
            print(f"Percentage of Player wins: {percentage:.1f}%") # Prints player winning statistics
        elif user_input == 4: # Exit
            break # Exits the entire project
        else:
            print("Invalid input! \nPlease enter an integer value between 1 and 4.")