# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
#오류 코드
# words = list(map(int, input().split()))
# print(words)

# 원인
# print(wordTraceback (most recent call last):
#   File "/Users/KIMSEONGYO1/Desktop/TIL/Python/Practice/예제_04.py", line 4, in <module>
#     words = list(map(int, input().split()))
# ValueError: invalid literal for int() with base 10: 'words'
# int 함수는 정수 타입의 문자열을 넣어야 한다.

#  수정
words = list(map(str, input().split()))
print(words)
