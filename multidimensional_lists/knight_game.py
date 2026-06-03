n = int(input())
board = []

for _ in range(n):
    board.append(list(input()))

#logic
knight_moves = [
    (-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)
]
knights_removed = 0

while True:
    max_attack = 0
    knights_to_remove = None

    for row in range(n):
        for column in range(n):
            if board[row][column] == "K":
                attack = 0
                for move_row,move_col in knight_moves:
                    next_row = row + move_row
                    next_column = column + move_col

                    if 0 <= next_row < n and 0 <= next_column < n:
                        if board[next_row][next_column] == "K":
                            attack += 1
                if attack > max_attack:
                    max_attack = attack
                    knights_to_remove = [row,column]
    if max_attack == 0:
        break
    row,column = knights_to_remove
    board[row][column] = "0"
    knights_removed += 1

print(knights_removed)
