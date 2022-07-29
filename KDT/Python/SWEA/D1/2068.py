t = int(input())

for i in range(t):
    n = map(int, input().split())
    m = max(n)
    print(f'#{i+1} {m}')