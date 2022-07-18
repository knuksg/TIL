# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# 원인
# number_list에 숫자를 넣을 때마다 total과 count가 함께 올라가야 하는데 
# count는 for문 밖에 있기 때문에 한 번 밖에 더해지지 않았다.
# '//' 대신에 '/'를 써야 한다.

#  수정
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)