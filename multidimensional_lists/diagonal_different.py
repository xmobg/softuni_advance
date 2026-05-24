n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondery_diagonal = [matrix[i][-1 -i] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondery_diagonal)))