from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
deque1 = deque()

for i in range(n):
    command = list(map(str, input().split()))
    if command[0] == "push_front":
        deque1.appendleft(command[1])
    elif command[0] == "push_back":
        deque1.append(command[1])
    elif command[0] == "pop_front":
        if deque1:
            print(deque1.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if deque1:
            print(deque1.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deque1))
    elif command[0] == "empty":
        if deque1:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if deque1:
            print(deque1[0])
        else:
            print(-1)
    else:
        if deque1:
            print(deque1[-1])
        else:
            print(-1)
