for t in range(int(input())):
    n, k = map(int, input().split())
    n_list = []
    for i in range(n):
        n_list.append(list(map(int, input().split())))
    result = 0
    # 행부터 순회
    rst = []
    for r in range(n):
        cnt = 0
        for c in range(n):
            if n_list[r][c] == 1:
                cnt += 1
            else:
                rst.append(cnt)
                cnt = 0
        rst.append(cnt)
        cnt = 0
    for i in rst:
        if i == k:
            result += 1
    # 열부터 순회
    rst = []
    for c in range(n):
        cnt = 0
        for r in range(n):
            if n_list[r][c] == 1:
                cnt += 1
            else:
                rst.append(cnt)
                cnt = 0
        rst.append(cnt)
        cnt = 0
    for i in rst:
        if i == k:
            result += 1
    print(f'#{t+1} {result}')