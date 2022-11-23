import sys
input = sys.stdin.readline
heap = {}
for i in range(int(input())):
    age, name = input().split()
    heap[i] = ([int(age), i, name])
result = sorted(heap.values(), key=lambda x:(x[0], x[1]), reverse=True)
for i in range(len(heap)):
    a = result.pop()
    print(a[0], a[2])