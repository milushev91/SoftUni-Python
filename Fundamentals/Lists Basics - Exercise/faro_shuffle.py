cards = input().split()
times = int(input())

for _ in range(times):
    middle_cards = cards[1:len(cards) - 1] # 'two', 'three', 'four', 'five'
    middle = len(middle_cards) // 2
    
    shuffled_cards = []
    
    first_cards = middle_cards[:middle]
    second_cards = middle_cards[middle:]
    
    for idx in range(middle):
        shuffled_cards.extend([second_cards[idx], first_cards[idx]])

    cards[1:len(cards) - 1] = shuffled_cards

print(cards)
