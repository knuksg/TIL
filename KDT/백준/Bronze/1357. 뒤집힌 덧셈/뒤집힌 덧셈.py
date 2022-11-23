def Rev(n):
    return int(n[::-1])
X, Y = input().split()
print(Rev(str(Rev(X)+Rev(Y))))