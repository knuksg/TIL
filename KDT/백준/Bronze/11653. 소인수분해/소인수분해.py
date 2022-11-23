n = int(input())
cnt = 2
while n != 1:
    if n % cnt == 0:
        print(cnt)
        n /= cnt
    else:
        cnt += 1