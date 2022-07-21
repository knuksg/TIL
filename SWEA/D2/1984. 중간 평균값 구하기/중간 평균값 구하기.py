t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    print(f'#{i+1} {(sum(n) - max(n) - min(n)) / 8:.0f}')