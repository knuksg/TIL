TaeBo = input()
new_TaeBo = TaeBo.replace('=', '')
print(new_TaeBo.index('('), len(new_TaeBo)-new_TaeBo.index(')')-1)