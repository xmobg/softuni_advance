n_rows,n_cols = [int(x) for x in input().split(", ")]
matrix = []
total = 0

for _ in range(n_rows):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)
    total += sum(data)

print(total)
print(matrix)