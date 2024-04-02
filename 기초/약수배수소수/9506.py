while True:
    n = int(input())
    result = n
    n_list = []
    if n == -1:
        break
    else:
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                n_list.append(i)
                result -= i
        if result == 0:
            print(f"{n} = ", end="")
            for i in range(len(n_list) - 1):
                print(f"{n_list[i]} + ", end="")
            print(n_list[-1])
        else:
            print(f"{n} is NOT perfect.")
