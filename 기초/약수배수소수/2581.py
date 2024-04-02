m = int(input())
n = int(input())

prime_list = []

for i in range(m, n+1):
    if(i == 1):
        continue
    for j in range(2, i//2 + 1):
        if(i % j == 0):
            break
    else:
        prime_list.append(i)

if(len(prime_list) > 0):
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)

