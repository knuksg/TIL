import heapq
list_ = []
set_ = set()
for _ in range(int(input())):
    x = input()
    set_.add((len(x), x))
for i in set_:
    heapq.heappush(list_, i)
for i in range(len(list_)):
    print(heapq.heappop(list_)[1])