
clothes = list(map(int, input().split()))

rack_capacity = int(input())


racks_count = 1  
current_load = 0  

while clothes:
    
    item = clothes.pop()


    if current_load + item <= rack_capacity:
        current_load += item
    else:
        racks_count += 1
        current_load = item

print(racks_count)
