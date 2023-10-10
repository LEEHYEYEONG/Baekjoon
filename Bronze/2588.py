a = int(input())
b = int(input())

b1 = b//100 #3
b2 = (b//10)%10 #8
b3 = b%10 #5

print(a*b3)
print(a*b2)
print(a*b1)
print(a*b3 + a*b2*10 + a*b1*100)