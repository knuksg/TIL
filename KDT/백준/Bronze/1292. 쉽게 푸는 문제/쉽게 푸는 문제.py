a, b = map(int, input().split())
number_list = []
while len(number_list) < b:
    for i in range(1, b+1):
        for j in range(i):
            number_list.append(i)
print(sum(number_list[a-1:b]))