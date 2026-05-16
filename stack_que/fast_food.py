from collections import deque

food_quantity = int(input())

orders = deque(map(int,input().split()))
print(max(orders))
while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left:", *orders)
