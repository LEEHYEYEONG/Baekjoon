n = int(input())
number_list = list(map(int, input().split()))
result = 0
for i in number_list:
    division = 0
    for j in range(i, 0, -1):
        if(i % j == 0):
            division += 1
    if(division == 2):
        result +=1

print(result)


