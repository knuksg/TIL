cnt = 0
for _ in range(int(input())):
    word = list(input())
    w = word[0]
    list_ = {w: 1}
    for i in range(len(word)):
        if word[i] != w:
            w = word[i]
            list_[w] = list_.get(w, 0) + 1
    if sorted(list_.items(), key=lambda x:x[1])[-1][1] == 1:
        cnt += 1
print(cnt)