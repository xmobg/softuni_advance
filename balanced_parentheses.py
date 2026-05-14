expression = input()

parenthesses = {
    "(" : ")",
    "{" : "}",
    "[" : "]"
}
stack = []

for char in expression:
    if char in parenthesses:
        stack.append(char)
    elif char in parenthesses.values():
        if not stack:
            print("NO")
            break
        last_operator = stack.pop()
        if parenthesses[last_operator] != char:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")