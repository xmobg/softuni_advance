from collections import deque

kids = deque(input().split())

rounds = int(input())

while len(kids) > 1:
    kids.rotate(-(rounds - 1))
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")