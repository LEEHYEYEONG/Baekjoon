n = int(input())

sum = 0

x_list = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        else:
            sum += (x_list[i] * x_list[j])
            
print(sum)