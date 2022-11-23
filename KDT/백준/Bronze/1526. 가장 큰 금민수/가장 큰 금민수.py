n = int(input())
for i in range(n,-1,-1):
    if len(set(str(i)) - set(['4', '7'])) == 0:
        print(i)
        break