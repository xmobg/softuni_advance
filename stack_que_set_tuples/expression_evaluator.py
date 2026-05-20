from collections import deque
expression = input().split()
numbers_queue = deque()
for token in expression:
    if token in ["+", "-", "*", "/"]:
        result = numbers_queue.popleft()

        while numbers_queue:
            next_number = numbers_queue.popleft()
            if token == "+":
                result += next_number
            elif token == "-":
                result -= next_number
            elif token == "*":
                result *= next_number
            elif token == "/":
                result //= next_number

        numbers_queue.append(result)
    else:
        numbers_queue.append(int(token))
print(numbers_queue.popleft())
