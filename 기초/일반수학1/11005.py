n, b = map(int, input().split())
remainder_list = []

num = 0
while n != 0:
    share = n // b
    remainder = n % b
    if remainder >= 10:
        remainder = chr(remainder + 55)
    else:
        remainder = str(remainder)
    remainder_list.append(remainder)
    n //= b

remainder_list = "".join(reversed(remainder_list))
print(remainder_list)

# nums='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# N,B=map(int,input().split())
# ans=''

# while N:
#     ans+=nums[N%B]
#     N//=B

# print(ans[::-1])
