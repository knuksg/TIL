# 예제 03. [오류 해결] 입력 받기
# 문제
# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# numbers = input().split()
# print(sum(numbers))

# 원인
# Traceback (most recent call last):
#   File "/Users/KIMSEONGYO1/Desktop/TIL/Python/Practice/예제_03.py", line 8, in <module>
#     print(sum(numbers))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sum(+) 함수는 int와 str 간의 합을 지원하지 않기 때문이다.

# 수정
numbers = map(int, input().split())
print(sum(numbers))