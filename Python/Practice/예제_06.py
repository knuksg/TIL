# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 원인
# Traceback (most recent call last):
#   File "/Users/KIMSEONGYO1/Desktop/TIL/Python/Practice/예제_05 copy.py", line 7, in <module>
#     answer.append(number * 2)
# AttributeError: 'tuple' object has no attribute 'append'
# tuple은 append 함수를 지원하지 않는다.

#  수정
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)