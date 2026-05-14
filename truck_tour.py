from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    fuel,distance = [int(x) for x in  input().split()]
    pumps.append({"fuel": fuel,"distance":distance})

start_position = 0
stops = 0

while stops < pumps_num:
    current_fuel = 0
    for i in range(pumps_num):
        current_fuel += pumps[i]["fuel"]
        distance = pumps[i]["distance"]
        if current_fuel < distance:
            stops  = 0
            pumps.rotate(-1)
            start_position += 1
            break
        current_fuel -= distance
        stops += 1
print(start_position)