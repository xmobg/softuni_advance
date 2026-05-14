clothes = list(map(int,input().split()))
rack_capacity = int(input())

racks = 0

while clothes:
    racks += 1
    current_rack_capacity = rack_capacity
    while clothes and current_rack_capacity >= clothes[-1]:
        current_rack_capacity -= clothes.pop()


print(racks)
