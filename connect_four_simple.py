"""
[[---],
[---].
[---]]

board [0] -> [-,-,-,]
board[1] -> [-,-,-]
board[2][2] -> "x"

"""

def generate_board(row: int, col: int) -> list[list]: # Creates the beard
    return [["-" for i in range(col)] for j in range(row)] # List comprehension in list comprehension

def main():
    board = generate_board(3,3)
    token(board, "x", 0, 0)
    token(board, "x", 1, 0)
    token(board, "x", 2, 0)
    print_board(board)
    print(winner(board))


def print_board(board: list[list]):
    for row in board:
        for col in row:
            print(col, end = "")
        print()

def token(board: list[list], token: str, row: int, col: int) -> None:
    board[row][col] = token

def winner(board: list[list]) -> str:
    # checking rows for a winner
    """
    xxx
    0x0
    00x

    first column:
    row[0][0], row[1][0], row[2][0]
    """
    for i in range(len(board)): # Returns 0, 1, 2 (number of rows)
        first_row = board[i][0]
        for j in range(len(board[0])): # returns 0,1,2 (Number of columns)
            if board[j][i] != first_row or board [j][i] == "-":
                break
            else:
                return first_row

    for row in board:
        first_col = row[0]
        for col in row[1:] or col == "-": # checking every character past the first ine
            if col != first_col:
                break
            else:
                return first_col

if __name__ == "__main__":
   main()
