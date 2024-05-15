for i in range(10):
    n = int(input())
    boxs = list(map(int, input().split()))

    for j in range(n):
        a, b = max(boxs), min(boxs)
        boxs[boxs.index(a)] = boxs[boxs.index(a)] - 1
        boxs[boxs.index(b)] = boxs[boxs.index(b)] + 1

    print(f"#{i+1} {max(boxs)-min(boxs)}")
