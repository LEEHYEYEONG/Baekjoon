# n, m = map(int, input().split())
# a = [[0 for col in range(m)] for row in range(n)]
# b = [[0 for col in range(m)] for row in range(n)]

# for i in range(n):
# 	a[i] = list(map(int, input().split()))
	
# for i in range(n):
# 	b[i] = list(map(int, input().split()))
	
# for i in range(n):
# 	for j in range(m):
# 		a[i][j] += b[i][j]
# 	print(*a[i])

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]
	
for i in range(n):
	for j in range(m):
		a[i][j] += b[i][j]
	print(*a[i])