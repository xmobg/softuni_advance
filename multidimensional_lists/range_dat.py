matrix = []
targets = 0

for row in range(5):
    current_row = input().split()
    matrix.append(current_row)

    if "A" in current_row:
        player_row = row
        player_col = current_row.index("A")

    targets += current_row.count("x")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())

hit_targets = []

for _ in range(n):

    command_data = input().split()
    command = command_data[0]
    direction = command_data[1]

    row_change, col_change = directions[direction]

    if command == "move":

        steps = int(command_data[2])

        new_row = player_row + row_change * steps
        new_col = player_col + col_change * steps

        if 0 <= new_row < 5 and 0 <= new_col < 5:
            if matrix[new_row][new_col] == ".":

                matrix[player_row][player_col] = "."

                player_row = new_row
                player_col = new_col

                matrix[player_row][player_col] = "A"

    elif command == "shoot":

        shoot_row = player_row + row_change
        shoot_col = player_col + col_change

        while 0 <= shoot_row < 5 and 0 <= shoot_col < 5:

            if matrix[shoot_row][shoot_col] == "x":

                matrix[shoot_row][shoot_col] = "."
                hit_targets.append([shoot_row, shoot_col])

                targets -= 1

                break

            shoot_row += row_change
            shoot_col += col_change

    if targets == 0:
        print(f"Training completed! All {len(hit_targets)} targets hit.")
        break

else:
    print(f"Training not completed! {targets} targets left.")

for target in hit_targets:
    print(target)