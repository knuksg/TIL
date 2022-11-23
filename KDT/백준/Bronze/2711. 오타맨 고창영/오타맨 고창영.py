T = int(input())
for i in range(T):
    ota, word = input().split()
    # 4, MISSPELL
    new_word = ' '.join(word).split()
    # ['M', 'I', 'S', ...]
    new_word.pop(int(ota)-1)
    # ['I' , 'S', ...]
    print(''.join(new_word))
    # is...