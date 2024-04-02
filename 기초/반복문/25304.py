x = int(input())
n = int(input())

price_sum = 0

for i in range(n):
	a, b = map(int, input().split())
	price_sum += a*b

if(x == price_sum):
	print("Yes")
else:
	print("No")
