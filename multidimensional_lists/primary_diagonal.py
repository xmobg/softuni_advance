n = int(input())
matrix = []
for i in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)
col_sum = 0
for row_index in range(n):
    for col_index in range(n):
        if row_index == col_index:
           col_sum += matrix[row_index][col_index]

print(col_sum)

