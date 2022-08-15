cnt = 0
n = int(input())
while n:
    if n%5 == 0:
        cnt += n//5
        break
    else:
        cnt += 1
        n -= 3
if n < 0:
    print(-1)
else:
    print(cnt)