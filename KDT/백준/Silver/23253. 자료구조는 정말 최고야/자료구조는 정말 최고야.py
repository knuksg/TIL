import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]*(n+1)
for i in range(m):
    heap_n = int(input())
    heaps = list(map(int, input().split()))
    for j in range(heap_n-1):
        if heaps[j] < heaps[j+1]:
            print('No')
            exit(0)
print('Yes')