rows = int(input())
matrix = []

for _ in range(rows):
    row = input().split()
    numbers = []
    for x in row:
        numbers.append(int(x))
    matrix.append(numbers)
while True:
    command = input()
    if command == "END":
        break

    action,row, col,value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Substract":
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row)
