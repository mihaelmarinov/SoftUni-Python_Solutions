cards = input().split()
shuffles = int(input())

top_bottom_card = []

top_bottom_card.append(cards[0])
top_bottom_card.append(cards[-1])
cards.remove(cards[0])
cards.remove(cards[-1])

rearranged = []


def card_sorter(cards):
    first_half = [cards[a] for a in range(0, int(len(cards) / 2))]
    second_half = [cards[b] for b in range(int(len(cards) / 2), len(cards))]

    while len(first_half) != 0 and len(second_half) != 0:
        rearranged.append(second_half[0])
        second_half.remove(second_half[0])
        rearranged.append(first_half[0])
        first_half.remove(first_half[0])


for i in range(shuffles):
    card_sorter(cards)
    cards = rearranged.copy()
    rearranged.clear()

cards.insert(0, top_bottom_card[0])
cards.append(top_bottom_card[-1])

print(cards)
