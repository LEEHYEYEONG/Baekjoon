n, x = map(int, input().split())

# 한 줄로 리스트를 받기 
n_list = [int(n) for n in input().split()]

# x보다 작은 수를 출력 
newList = [i for i in n_list if i<x]
print(*newList)