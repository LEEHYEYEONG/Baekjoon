import sys
from collections import deque
input = sys.stdin.readline

queue =deque([])

n = int(input())
for i in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if queue:
            print(queue[-1])
        else:
            print(-1)
