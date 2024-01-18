from collections import deque

n, k = map(int, input().split())
dist = [0] * 100001

need_visited = deque()
need_visited.append(n)

way = 0

while need_visited:
    node = need_visited.popleft()

    if node == k:
        way = dist[node]
        continue

    for i in (node - 1, node + 1, node * 2):
        if 0 <= i <= 100000 and dist[i] == 0:
            dist[i] = dist[node] + 1
            need_visited.append(i)

print(way)
