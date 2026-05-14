from collections import deque
que = deque()
while True:
    string = input()
    if string == "End":
        print(f"{len(que)} people remaining.")
        break
    elif string == "Paid":
        for _ in range(len(que)):
            print(que.popleft())
    else:
        que.append(string)
