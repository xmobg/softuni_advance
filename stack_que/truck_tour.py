n = int(input())

tank = 0
total = 0
start = 0

for i in range(n):
    petrol, distance = map(int, input().split())
    diff = petrol - distance

    tank += diff
    total += diff

    if tank < 0:
        start = i + 1
        tank = 0

print(start)
