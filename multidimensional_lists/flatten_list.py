data = input()
temp = []
matrix = data.split("|")

for matrix in reversed(matrix):
    if matrix:
        numbers = matrix.split()
        temp.extend(numbers)


result = ' '.join(temp)
print(result)