matrix = []
n, m = map(int, input().split())
for _ in range(n):
    matrix.append(list(map(int, input().split())))
k = int(input())
for _ in range(k):
    sum_ = 0
    i, j, x, y = map(int,input().split())
    for row in range(i-1,x):
        for col in range(j-1,y):
            sum_ += matrix[row][col]
    print(sum_)