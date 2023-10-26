n, b = input().split()
print(int(n, int(b)))
n = list(n)
n.reverse()

b = int(b)
n_sum = 0
for i in range(len(n)):
    if ord(n[i]) - 65 >= 0:
        n_sum += b**i * (ord(n[i]) - 55)
    else:
        n_sum += b**i * (int(n[i]))

print(n_sum)
