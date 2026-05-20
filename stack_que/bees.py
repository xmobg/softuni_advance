from collections import deque


bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0


while bees and nectar:

    if nectar[-1] < bees[0]:
        nectar.pop()  
    else:

        symbol = symbols.popleft()
        bee = bees.popleft()
        current_nectar = nectar.pop()

        if symbol == "+":
            total_honey += abs(bee + current_nectar)
        elif symbol == "-":
            total_honey += abs(bee - current_nectar)
        elif symbol == "*":
            total_honey += abs(bee * current_nectar)
        elif symbol == "/":
            if current_nectar != 0:
                total_honey += abs(bee / current_nectar)


print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
