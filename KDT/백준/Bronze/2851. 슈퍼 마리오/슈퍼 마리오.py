mush = 0
mushroom = []
for i in range(10):
    mush += int(input())
    # 누적합
    mushroom.append(mush-100)
    # -100을 하고 절대값을 기준으로 정렬하면 100과 가장 가까운 누적합이 나온다.
    # [-90, -70, -40, 0, 50, 110, 180, 260, 350, 450]
result1 = 0
result2 = 100
for i in mushroom:
    if i < 0:
        result1 = i
    else:
        result2 = i
        break
if -result1 < result2:
    print(result1+100)
else:
    print(result2+100)