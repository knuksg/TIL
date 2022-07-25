t = int(input())

for i in range(t):
    w = input()
    w_list = list(w)
    w2_list = reversed(w_list)
    if list(w2_list) == w_list:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')