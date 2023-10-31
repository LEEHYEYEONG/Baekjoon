# n = int(input())
# check = 0
# sum = 0
# a_list = []
# b_list = []

# for i in range(1, n+1):
    
#     for j in range(1, i+1):
#         a_list.append(j)
#     for j in range(i, 0, -1):
#         b_list.append(j)
#     if(n <= sum):
#         break
#     sum += i
#     check+=1

# if(check % 2 != 0):
#     print(f"{b_list[n-1]}/{a_list[n-1]}")
# else:
#     print(f"{a_list[n-1]}/{b_list[n-1]}")

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')
