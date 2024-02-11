string = input()

n = int(input())
words = [input() for _ in range(n)]

for i in range(26):
    new = ""
    for j in string:
        if ord(j) - i < 97:
            new += chr(ord(j) - i + 26)
        elif ord(j) - i > 122:
            new += chr(ord(j) - i - 26)
        else:
            new += chr(ord(j) - i)

    for word in words:
        if word in new:
            print(new)
            break
