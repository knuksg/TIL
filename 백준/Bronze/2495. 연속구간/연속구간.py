cnt = 0
cnt_list = []
for _ in range(3):
    number = input()
    next_number = -1
    for i in range(len(number)):
        if number[i] == next_number:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0
            next_number = number[i]
    cnt_list.append(cnt)
    cnt = 0
    print(max(cnt_list)+1)
    cnt_list.clear()