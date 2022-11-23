n = int(input())
rst = n
cnt = 0

while True:
    if n >= 10:
        a = n%10*10
        b = (n//10+n%10)%10
        n = a + b
    else:
        a = n*10
        b = n
        n = a + b
    if n != rst:
        cnt += 1
        continue
    else:
        cnt += 1
        break
print(cnt)