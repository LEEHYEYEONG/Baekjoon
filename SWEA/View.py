for i in range(10):
    answer = 0
    N = int(input())
    buildings = list(map(int, input().split()))

    for j in range(2, N - 2):
        current = buildings[j]
        current_list = [
            buildings[j - 2],
            buildings[j - 1],
            buildings[j + 1],
            buildings[j + 2],
        ]

        if current >= max(current_list):
            answer += current - max(current_list)

    print(f"#{i+1} {answer}")
