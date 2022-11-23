k = int(input())
k_list = []
for i in range(k):
    n = int(input())
    if n != 0:
        k_list.append(n)
    else:
        k_list.pop()
print(sum(k_list))