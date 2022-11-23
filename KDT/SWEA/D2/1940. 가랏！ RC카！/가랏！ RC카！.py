t = int(input())
for i in range(t):
    N = int(input())
    rst = 0
    speed = 0
    for ii in range(N):
        a = list(map(int, input().split()))
        if a[0] == 1:
            speed += a[1]
            rst += speed
        elif a[0] == 2:
            if a[1] > speed:
                speed = 0
            else:
                speed -= a[1]
                rst += speed
        else:
            rst += speed
    print(f'#{i+1} {rst}')