from typing import Counter
number = []
n = int(input())
for _ in range(n):
    number.append(int(input()))
new_number = sorted(number)
if -1 < sum(number)/n < 0:
    print(0)
else:
    print(f'{sum(number)/n:.0f}')
print(new_number[n//2])
count_ = Counter(number)
new_count = []
for i in count_:
    if count_[i] == max(count_.values()):
        new_count.append(i)
new_count = sorted(new_count)
if len(new_count) == 1:
    print(*new_count)
else:
    print(new_count[1])
print(max(number)-min(number))