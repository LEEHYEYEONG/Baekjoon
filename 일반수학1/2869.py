import math

a, b, v = map(int, input().split())

if(v-a < 0):
    print(1)
else:
    print(math.ceil((v-a) / (a-b)) + 1)

# day = 1

# while(v > 0):
#     v-=a
#     if(v<=0):
#         break
#     v+=b
#     day+=1
# print(day)

