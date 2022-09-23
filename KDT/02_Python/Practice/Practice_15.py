# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = 'banana'
# apple # 0
# kiwi # -1

for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break
else:
    print('-1')

# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

word = 'HappyHacking'
# banana # 1 3 5
# kiwi # 

rst = []

for i in range(len(word)):
    if word[i] == 'a':
        rst.append(i)
print(rst)