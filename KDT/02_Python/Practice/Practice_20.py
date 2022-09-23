n = int(input())
rst = 0
while n!=0:
    rst += n%10
    n = n//10
print(rst)