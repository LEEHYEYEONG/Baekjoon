n, m = map(int, input().split())
card = list(map(int, input().split()))

num_list = []

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            card_sum = card[i] + card[j] + card[k]
            if card_sum > m:
                continue
            else:
                num_list.append(m - card_sum)

print(m - min(num_list))
