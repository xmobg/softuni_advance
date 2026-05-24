n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondery_diagonal = [matrix[i][-1 -i] for i in range(n)]

print(f"Primary diagonal: {', ' .join(map(str, primary_diagonal ))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondery_diagonal ))}. Sum: {sum(secondery_diagonal)}")
