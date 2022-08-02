for i in range(int(input())):
    a, b = map(int, input().split())
    if a + b < 24:
        print(f'#{i+1} {a+b}')
    else:
        print(f'#{i+1} {(a+b)%24}')