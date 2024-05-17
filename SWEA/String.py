for i in range(10):
    n = int(input())

    word = input()
    string = input()

    count = 0

    for j in range(len(string)):
        if string[j : j + len(word)] == word:
            count += 1

    print(f"#{i+1} {count}")
