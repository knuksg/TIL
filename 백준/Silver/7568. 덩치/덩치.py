N = int(input())
list_ = [] # 키와 몸무게를 담을 리스트.
result_list = [] # 덩치가 더 큰 사람을 기록할 리스트.
for i in range(N): 
    # N번만큼 리스트에 담는다.
    x, y = map(int, input().split())
    list_.append([x, y]) 
    # 리스트의 형태는 [[x, y], [x2, y2], ...], 리스트 안의 리스트.
for i in range(len(list_)):
    result = 0
    for j in range(len(list_)): 
        # 리스트의 인덱스 i의 키와 몸무게를 다른 리스트와 비교한다.
        if list_[i][0] < list_[j][0] and list_[i][1] < list_[j][1]: 
            result += 1 
            # 비교한 값을 담고, 다 비교하면 최종 리스트에 기록, 변수는 초기화한다.
    result_list.append(result)
for i in result_list: 
    # 덩치 등수는 자신보다 큰 덩치의 사람 + 1이라고 했으므로 1을 더해준다.
    print(i+1, end=' ')