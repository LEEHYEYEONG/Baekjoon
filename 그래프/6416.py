import sys
from collections import defaultdict

input = sys.stdin.readline


while True:
    # -1 -1이 나올때까지 입력받도록
    tree = defaultdict(list)
    count = 1
    while True:
        # 0 0 이 나올때까지 입력받도록
        a = list(map(int, input().split()))
        test = False
        for i in range(len(a)):
            if i % 2 == 1:
                if a[i] == 0 and a[i - 1] == 0:
                    test = True
                    break
                tree[a[i]].append(a[i - 1])
                if len(tree[a[i]]) > 1:
                    print("Case", count, "is not a tree")
                    test = True
                    break

        if test:
            count += 1
            break

        print("Case", count, "is a tree")
