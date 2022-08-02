import sys
input = sys.stdin.readline
import heapq
heap = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        if not len(heap):
            print(0)
        else:
            print(heapq.heappop(heap))