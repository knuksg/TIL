word = input()
new_word = word.replace('c=', 'w').replace('c-', 'w').replace('dz=', 'w').replace('d-', 'w').replace('lj', 'w').replace('nj', 'w').replace('s=', 'w').replace('z=', 'w')
print(len(new_word))