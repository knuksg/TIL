import heapq
n = int(input())
n_ = []
for i in range(n):
    heapq.heappush(n_, int(input()))
n_ = sorted(n_)
for i in range(n-1,-1,-1):
    print(n_[i])