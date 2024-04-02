# a, b = map(str, input().split())
# new_a = int(a[::-1])
# new_b = int(b[::-1])
# print(max(new_a, new_b))

a, b = input().split()
# print(max("".join(reversed(a)), "".join(reversed(b))))
print(type(reversed(a)), reversed(b))
