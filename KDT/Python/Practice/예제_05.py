# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
# number = 22020718
# print(len(number))

# 원인
# Traceback (most recent call last):
#   File "/Users/KIMSEONGYO1/Desktop/TIL/Python/Practice/예제_05.py", line 5, in <module>
#     print(len(number))
# TypeError: object of type 'int' has no len()
# int 타입은 길이를 구할 수 없다.

#  수정
number = 22020718
print(len(str(number)))