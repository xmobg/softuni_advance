from collections import deque


water_quantity = int(input())


people_queue = deque()


while True:
    name = input()
    if name == "Start":
        break
    people_queue.append(name)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):

        _, liters_to_add = command.split()
        water_quantity += int(liters_to_add)
    else:

        wanted_liters = int(command)
        current_person = people_queue.popleft()

        if wanted_liters <= water_quantity:
            water_quantity -= wanted_liters
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait")

print(f"{water_quantity} liters left")