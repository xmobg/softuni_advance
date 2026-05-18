sets = input().split()

n = int(sets[0])
m = int(sets[1])
numbers_in_n = set()
numbers_in_m = set()
for _ in range(n):
    numbers_in_n.add(int(input()))
for _ in range(m):
    numbers_in_m.add(int(input()))

for num in numbers_in_n.intersection(numbers_in_m):
    print(num)
