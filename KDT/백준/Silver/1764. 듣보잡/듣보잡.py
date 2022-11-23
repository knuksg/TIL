n, m = map(int, input().split())
n_dic = {}
for i in range(n):
    n_dic[input()] = 1

for i in range(m):
    see = input()
    n_dic[see] = n_dic.get(see, 0) + 1
new_n_dic = []
for i in n_dic:
    if n_dic[i] == 2:
        new_n_dic.append(i)
print(len(new_n_dic))
new_n_dic = sorted(new_n_dic)
for i in new_n_dic:
    print(i)