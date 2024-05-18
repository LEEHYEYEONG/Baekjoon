for i in range(10):
    test = int(input())

    n, m = map(int, input().split())

    def multiple(n, m):
        if m == 2:
            return n * n
        elif m == 1:
            return n
        else:
            return n * multiple(n, m - 1)

    print(f"#{test} {multiple(n, m)}")

    # pow(n, m)
