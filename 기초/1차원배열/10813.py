n, m = map(int, input().split())
n_list = [i+1 for i in range(n)]
for i in range(m):
	a, b = map(int, input().split())
	n_list[a-1], n_list[b-1] = n_list[b-1], n_list[a-1]

print(*n_list)