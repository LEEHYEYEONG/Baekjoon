from collections import defaultdict, deque

num = int(input())
pair = int(input())

# 바이러스 걸린 컴퓨터 수
count = 0
graph = defaultdict(list)

for i in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (num + 1)
queue = deque([1])


# bfs
def bfs(graph, start):
    global count
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                count += 1


# dfs
def dfs(graph, start):
    global count
    visited[start] = 1

    for key in graph[start]:
        if visited[key] == 0:
            dfs(graph, key)
            count += 1


dfs(graph, 1)
# bfs(graph, 1)
print(count)
