def check_row_winner(board, current_sign):
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False


def check_column_winner(board, current_sign):
    for col_index in range(3):
        count = 0
        for row_index in range(3):
            if board[row_index][col_index] == current_sign:
                count += 1
        if count == 3:
            return True
    return False


def check_diag_winner(board, current_sign):
    count_primary = 0
    count_secondary = 0

    for index in range(3):
        if board[index][index] == current_sign:
            count_primary += 1
        if board[index][3 - index - 1] == current_sign:
            count_secondary += 1

    return count_primary == 3 or count_secondary == 3


def check_for_winner(board, current_sign):
    return (
        check_row_winner(board, current_sign)
        or check_column_winner(board, current_sign)
        or check_diag_winner(board, current_sign)
    )


def print_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")


board = [[" ", " ", " "] for _ in range(3)]

mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

player_one = input("Player one name: ")
player_two = input("Player two name: ")

player_one_sign = input(
    f"{player_one}, would you like to play with 'X' or 'O'? "
).upper()

while player_one_sign not in ["X", "O"]:
    print("Please enter either 'X' or 'O'.")
    player_one_sign = input(
        f"{player_one}, would you like to play with 'X' or 'O'? "
    ).upper()

player_two_sign = "O" if player_one_sign == "X" else "X"

print("\nThis is the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |\n")

print(f"{player_one} starts first!\n")

turn = 1
winner = False

print_board(board)

while turn <= 9:
    current_player = player_one if turn % 2 != 0 else player_two
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign

    print(f"\nIt's {current_player}'s turn ({current_sign})")

    try:
        position = int(input("Choose position (1-9): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if position not in mapper:
        print("Invalid position! Choose between 1 and 9.")
        continue

    row, col = mapper[position]

    if board[row][col] != " ":
        print("That position is already taken!")
        continue

    board[row][col] = current_sign
    print_board(board)

    if turn >= 5 and check_for_winner(board, current_sign):
        print(f"\n Congratulations {current_player}, you win!")
        winner = True
        break

    turn += 1

if not winner:
    print("\n It's a draw!")