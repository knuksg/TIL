from collections import Counter
list_ = []
for _ in range(10):
    list_.append(int(input()))
list_counter = Counter(list_).most_common()
print(sum(list_)//10, list_counter[0][0], sep='\n')