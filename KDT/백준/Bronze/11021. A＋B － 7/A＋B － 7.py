import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    r = list(map(int, input().split()))
    print(f'Case #{i+1}: {r[0]+r[1]}', sep='')