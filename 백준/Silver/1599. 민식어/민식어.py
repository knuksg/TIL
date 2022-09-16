minsik = {'a': '1',
 'b': '2',
 'k': '3',
 'd': '4',
 'e': '5',
 'g': '6',
 'h': '7',
 'i': '8',
 'l': '9',
 'm': 'a',
 'n': 'b',
 'z': 'c',
 'o': 'd',
 'p': 'e',
 'r': 'f',
 's': 'g',
 't': 'h',
 'u': 'i',
 'w': 'j',
 'y': 'k'}

list_ = []

for _ in range(int(input())):
    word = input()
    word = word.replace('ng', 'z')
    new_word = ''
    for i in range(len(word)):
        new_word += minsik[word[i]]
    list_.append((new_word, word))

list_ = sorted(list_)

for i in range(len(list_)):
    print(list_[i][1].replace('z', 'ng'))