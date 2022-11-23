n, m = map(int, input().split())
dic_ = dict()
for i in range(n):
    dic_[input()] = 1
cnt = 0
for i in range(m):
    word = input()
    if dic_.get(word) == True:
        cnt +=1
print(cnt)