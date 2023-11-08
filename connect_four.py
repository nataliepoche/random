def initialize_board(row, col): # turn each space into "-"
    return [["-" for i in range(col)] for j in range(row)]
def print_board(board): # prints the board
    for row in board[::-1]: # reverses the board
        for col in row:
            print(col, end = "")
        print()
def insert_chip(board, col, row, chip_type):
    board[row][col] = chip_type # replaces "-" with the chip type
    return board[row]

def check_if_winner(board, player_row, player_col, chip_type): # Checks for the winner
   # len(board) returns rows
   # len(board[0]) returns columns

   # check horizontally
   for c in range(len(board[0])): # separates the columns
       count = 0
       for r in range(len(board)): # goes through each row
           if board[r][c] == chip_type: # checks if the row matches chip type
               count += 1 # records if row matches chip type
               if count == 4: # if consecutive 4 matches, ends
                   return True
           else: # if no match chip type, checker resets
               count = 0 # resets checker

    # checks vertically
   for r in range(len(board)): # Separates the rows
       count = 0
       for c in range(len(board[0])): # Goes through each column
           if board[r][c] == chip_type: # checks to see if chip type matches
               count += 1 # records chip type match
               if count == 4: # If four consecutive matches, game ends
                   return True
           else: # if no match, checker resets
               count = 0 # resets checker
   return False

if __name__ == "__main__":
    row = int(input("What would you like the height of the board to be?")) # Inputs the row
    col = int(input("What would you like the length of the board to be?")) # inputs the column
    board = initialize_board(row, col) # Initializes the board
    print_board(board) # Prints the board
    chip_type = 0 # Keeps track of the chip
    print("Player 1: x")
    print("Player 2: o")
    condition = True
    player_turn = 0 # # Keeps track of the player
    player_col = 0
    player_row = 0
    check_row = 0
    while condition == True:
        if player_turn % 2 == 0: # determines player 1
            player = 1 # Keeps track of player 1
            chip_type = "x" # assigns chip value
            player_col = int(input(f"Player {player}: Which column would you like to choose?"))
        elif player_turn % 2 > 0: # determines player 2
            player = 2 # keeps track of player 1
            chip_type = "o" # assigns chip value
            player_col = int(input(f"Player {player}: Which column would you like to choose?"))
        while board[player_row][player_col] != "-": # Makes sure previously placed chip isn't replaced
                player_row += 1 # adds
        player_turn += 1
        check_row = insert_chip(board, player_col, player_row, chip_type)
        print_board(board)
        if check_if_winner(board, check_row, player_col, chip_type):
            print(f"Player {player} won the game!")
            condition = False
        chip_count = 0
        for r in board: # lists out board
            for c in r: # goes though each column
                if c != "-": # if the space is not "-", counts
                    chip_count += 1 # records taken space
        if chip_count == (col * row): # checks if there's any space on board
            print("Draw. Nobody wins.")
            condition = False
        chip_count = 0 # resets the chip count
        player_row = 0