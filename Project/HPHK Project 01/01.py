with open('3회차/김선교/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

with open('01.txt', 'w', encoding='utf-8') as f2:
    f2.write(str(len(text)))