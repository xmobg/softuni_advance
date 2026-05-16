expression = input()
stack = []
brackets_map = {')': '(', ']': '[', '}': '{'}
is_balanced = True

for char in expression:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if not stack:
            is_balanced = False
            break
        
        last_open = stack.pop()
        if last_open != brackets_map[char]:
            is_balanced = False
            break

if is_balanced and not stack:
    print("YES")
else:
    print("NO")
