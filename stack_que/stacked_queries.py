n = int(input())

stack = []

functions = {
    "1": lambda n: stack.append(int(n)),
    "2": lambda : stack.pop() if stack else None,
    "3": lambda : print(max(stack)) if stack else None,
    "4": lambda : print(min(stack)) if stack else None,

}

for _ in range(n):
    query = input().split()
    functions[query[0]](*query[1:])

print(*reversed(stack), sep=", ")
