w_list = []
k_list = []
for i in range(10):
    w_list.append(int(input()))
for i in range(10):
    k_list.append(int(input()))
w_list.sort()
k_list.sort()
print(sum(w_list[7:10]), sum(k_list[7:10]))