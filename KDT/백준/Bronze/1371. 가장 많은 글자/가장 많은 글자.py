dic_ = {}
while True:
    try:
        word = input().replace(' ', '')
        for w in word:
            dic_[w] = dic_.get(w, 0) + 1
    except:
        break
sorted_dic = sorted(dic_.items(), key=lambda x:(-x[1], x[0]))
for i in sorted_dic:
    if i[1] == sorted_dic[0][1]:
        print(i[0], end='')