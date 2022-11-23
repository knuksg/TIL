for i in range(1, int(input())+1):
    l, u, x = map(int, input().split())
    if x > u:
        print(f'#{i} -1')
    elif x >= l:
        print(f'#{i} 0')
    else:
        print(f'#{i} {l-x}')