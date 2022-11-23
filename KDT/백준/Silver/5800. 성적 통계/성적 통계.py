for i in range(int(input())):
    number = list(map(int, input().split()))
    n = number[0]
    n_number = sorted(number[1:])
    mx = max(n_number)
    mn = min(n_number)
    gap = 0
    for j in range(1, len(n_number)):
        if n_number[j] - n_number[j-1] >= gap:
            gap = n_number[j] - n_number[j-1]
    print('Class', i+1)
    print(f'Max {mx}, Min {mn}, Largest gap {gap}')