import sys


def part_str(s, t):
    for i in s:
        if i not in t:
            return "No"
        t = t[t.index(i) + 1 :]
    return "Yes"


while True:
    try:
        s, t = map(str, sys.stdin.readline().split())
        print(part_str(s, t))

    except:
        break
