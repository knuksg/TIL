for t in range(int(input())):
    n, m = map(int, input().split())
    n_list = []
    for i in range(n):
        n_list.append(list(map(int, input().split())))
    sum_ = []
    sum_list = []
    for r in range(n-m+1):
        for c in range(n-m+1):
            for r1 in range(m):
                for c1 in range(m):
                    sum_.append(n_list[r+r1][c+c1])
            sum_list.append(sum(sum_))
            sum_ = []
    print(f'#{t+1} {max(sum_list)}')