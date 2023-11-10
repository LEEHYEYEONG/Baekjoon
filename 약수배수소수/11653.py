n = int(input())
if(n == 1):
    print()

while(n != 1):  
    for i in range(2, n//2 + 1):
        if(n % i == 0):
            for j in range(2, i//2 + 1):
                if(i % j == 0):
                    break
            else:
                while(n%i != 0):
                    print(i)
                    n //= i


