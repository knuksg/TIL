import sys

sys.stdin = open("_암호문1.txt")

for i in range(10):
    n = int(input())
    test_case = list(input().split())
    c = int(input())
    # I를 기준으로 스플릿, 첫 자리 '' 빼고 나머지는 다 '삽입할 자리, 삽입할 개수, 삽입할 숫자들'의 리스트.
    c_list = input().split('I')
    command_list = []
    for j in range(c+1):
        # 첫 자리 '' 빼고 리스트에 넣기.
        if j != 0:
            command_list.append(c_list[j].split())
    for j in command_list:
        # 삽입할 개수만큼 반복
        for x in range(int(j[1])):
            # 테스트 케이스의 삽입할 자리에 삽입할 숫자들을 뒤에서부터 집어넣기.
            # (뒤에서부터 넣어야 삽입할 자리부터 순차적으로 삽입되니까.)
            test_case.insert(int(j[0]), j[len(j)-x-1])
    print(f'#{i+1}', end=' ')
    # 테스트 케이스 10개만 출력하기.
    for j in range(len(test_case)):
        if j == 9:
            print(test_case[j])
            break
        else:
            print(test_case[j], end=' ')