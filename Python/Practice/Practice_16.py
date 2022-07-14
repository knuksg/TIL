# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = 'apple'
# aeiou # 5
# zxcvb # 0

cnt = 0

for w in word:
    if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
        cnt += 1
print(cnt)