n = int(input())
name_set = set()

for _ in range(n):
    name = input()
    name_set.add(name)
for name in name_set:
    print(name)