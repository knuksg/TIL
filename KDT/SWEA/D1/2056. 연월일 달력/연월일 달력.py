t = int(input())

for i in range(t):
    m = input()
    n = list(m)
    for ii in range(len(n)):
        n[ii] = int(n[ii])
    if n[0]+n[1]+n[2]+n[3] == 0:
        print(f'#{i+1} -1')
    elif n[4]+n[5] == 0:
        print(f'#{i+1} -1')
    elif n[6]+n[7] == 0:
        print(f'#{i+1} -1')
    elif (n[4]*10)+n[5] > 12:
        print(f'#{i+1} -1')
    elif n[5] == 2 and (n[6]*10)+n[7] > 28:
        print(f'#{i+1} -1')
    elif n[5] in [1, 3, 5, 7, 8, 10, 12] and (n[6]*10)+n[7] > 31:
        print(f'#{i+1} -1')
    elif n[5] in [4, 6, 9, 11] and (n[6]*10)+n[7] > 30:
        print(f'#{i+1} -1')
    else:
        print(f'#{i+1} {n[0]}{n[1]}{n[2]}{n[3]}/{n[4]}{n[5]}/{n[6]}{n[7]}')
