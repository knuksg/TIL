import heapq
import sys
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    heapq.heappush(heap, int(input()))
for _ in range(len(heap)):
    print(heapq.heappop(heap))