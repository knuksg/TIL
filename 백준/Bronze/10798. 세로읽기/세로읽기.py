word = []
for i in range(5):
    word_word = ' '.join(input()).split()
    # ['A', 'A', 'B', 'C', 'D', 'D']
    while len(word_word) < 15:
        word_word.append('')
        # 각 줄의 문자는 최대 15줄이므로, 15줄이 안 될 경우 공백을 추가함.
    word.append(word_word)
# [['A', 'A', 'B', 'C', 'D', 'D', '', '', '', '', '', '', '', '', ''], 
#  ['a', 'f', 'z', 'z', '', '', '', '', '', '', '', '', '', '', ''], 
#  ['0', '9', '1', '2', '1', '', '', '', '', '', '', '', '', '', ''], 
#  ['a', '8', 'E', 'W', 'g', '6', '', '', '', '', '', '', '', '', ''], 
#  ['P', '5', 'h', '3', 'k', 'x', '', '', '', '', '', '', '', '', '']]
new_word = ''
# 단어를 담을 변수.
for j in range(15):
    for i in range(5):
        new_word += word[i][j]
        # 순서대로 각 줄의 문자들을 단어에 추가함.
print(new_word)