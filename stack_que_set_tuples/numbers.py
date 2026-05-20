numbers_one = set(int(x) for  x in input().split())
numbers_two = set(int(x) for  x in input().split())
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    type_ = command[1]
    current_numbers = [int(x) for x in command[2:]]
    if action == 'Add':
        if type_ == "First":
            numbers_one.update(current_numbers)
        elif type_ == "Second":
            numbers_two.update(current_numbers)
    elif action == 'Remove':
        if type_ == "First":
            numbers_one.difference_update(current_numbers)
        elif type_ == "Second":
            numbers_two.difference_update(current_numbers)
    elif action == 'Check' and type_ == "Subset":
        if numbers_one.issubset(numbers_two) or numbers_two.issubset(numbers_one):
            print("True")
        else:
            print("False")
print(*sorted(numbers_one), sep=", ")
print(*sorted(numbers_two), sep=", ")
