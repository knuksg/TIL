from collections import deque
card = deque(range(1, int(input())+1))
throw_card = []
while len(card) > 1:   
    throw_card.append(card.popleft())
    card.append(card.popleft())
print(*throw_card, *card)