import sys

sys.stdin = open("_반반.txt")

for i in range(int(input())):
    dic_ = {}
    s = input()
    for w in s:
        dic_[w] = dic_.get(w, 0) + 1
    # 알파벳이 2개가 아니라면
    if len(dic_) != 2:
        print(f'#{i+1} No')
    else:
        for word in dic_:
            # 알파벳의 개수가 2개가 아니라면
            if dic_[word] != 2:
                print(f'#{i+1} No')
        else:
            print(f'#{i+1} Yes')