n = int(input())
member = list(map(int, input().split()))
dic_ = {}
rst = 0
for i in range(n):
    if dic_.get(member[i]) != None:
        rst += 1
    else:
        dic_[member[i]] = 1
print(rst)