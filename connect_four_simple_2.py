# Takes in number of rows and columns and returns created board as a 2D list
def initialize_ttt_board(row: int, col: int) -> list[list]:
    return [["-" for i in range(col)] for j in range(row)]


# Prints the created board with the first row (board[0]) being at the top
def print_ttt_board(board: list[list]) -> None:
    for row in board:
        for col in row:
            print(col, end="")
        print()


# Insert the token into the specific row and column of the board
def insert_ttt_token(board: list[list], token: str, row: int, col: int) -> None:
    board[row][col] = token


# Check for a winner for the board by checking the columns and then the rows,
# returns the token of the winner, or "Nobody" if no winner was detected
def check_winner_ttt(board: list[list]) -> str:
    # Iterate over the number of columns
    for i in range(len(board[0])):
        # This is the first character of the column we're checking
        firstRow = board[0][i]
        # Iterate over the number of rows
        for j in range(len(board)):
            if board[j][i] != firstRow or board[j][i] == "-":
                break
        else:
            return firstRow

    # For each inner list of the outer list, i.e. each row of the board
    for row in board:
        # This is the first character of the row we're checking
        firstCol = row[0]
        # Checking every character past the first one
        for col in row[1:]:
            if col != firstCol or col == "-":
                break
        else:
            return firstCol

    return "Nobody"


def main():
    board = initialize_ttt_board(3, 3)
    insert_ttt_token(board, "X", 0, 0)
    insert_ttt_token(board, "X", 2, 0)
    insert_ttt_token(board, "X", 1, 0)

    insert_ttt_token(board, "X", 0, 1)
    insert_ttt_token(board, "O", 1, 1)
    insert_ttt_token(board, "O", 2, 1)

    insert_ttt_token(board, "O", 1, 2)
    print_ttt_board(board)
    print(f"The winner is {check_winner_ttt(board)}")


if __name__ == "__main__":
    main()