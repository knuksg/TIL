# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

word = 'banana'
word2 = list(word)
for i in range(len(word2)):
    word2[i] = chr(ord(word2[i]) - 32)
for i in word2:
    print(i, end='')