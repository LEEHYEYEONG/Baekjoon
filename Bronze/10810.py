#import sys

n, m = map(int, input().split())
n_list = [0 for i in range(n)] # 0으로 이루어진 리스트 만들기 

for i in range(m):
	#a, b, c = map(int, sys.stdin.readline().split())
	a, b, c = map(int, input().split())
	for j in range (a-1, b):
		n_list[j] = c

print(*n_list)
	
	