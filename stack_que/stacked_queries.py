n = int(input())

stack = []

for _ in range(n):
    query = input().split()

    command = query[0]

    match command:
        case "1":
            stack.append(int(query[1]))
        case "2":
            if stack:
                stack.pop()
        case "3":
            if stack:
                print(max(stack))
        case "4":
            if stack:
                print(min(stack))

print(", ".join(map(str, reversed(stack))))
