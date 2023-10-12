n, m = map(int, input().split())
n_list = [i+1 for i in range(n)]

for i in range(m):
	a, b = map(int, input().split())
	change_list = n_list[a-1:b]
	change_list.reverse()
	n_list[a-1:b] = change_list

print(*n_list)