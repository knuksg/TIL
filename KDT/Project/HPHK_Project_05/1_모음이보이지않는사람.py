import sys

sys.stdin = open("_모음이보이지않는사람.txt")

for i in range(int(input())):
    word = input()
    new_word = word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    print(f'#{i+1} {new_word}')