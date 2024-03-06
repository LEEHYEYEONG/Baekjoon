from collections import deque

n, k = map(int, input().split())
queue = deque([i + 1 for i in range(n)])

answer = []
index = 0

while queue:
    index += 1
    tmp = queue.popleft()
    if index % k != 0:
        queue.append(tmp)
    else:
        answer.append(tmp)

s = ", ".join(map(str, answer))
print("<" + s + ">")
