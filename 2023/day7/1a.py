from collections import Counter

hand_types = {"Five of a kind": [],  # example: 55555
              "Four of a kind": [],  # example: 5555A
              "Full house": [],  # example: 555AA
              "Three of a kind": [],  # example: 555AK
              "Two pair": [],  # example: 55AAK
              "One pair": [],  # example: 55AKQ
              "High card": []}  # example: 5AKQJ

hands = {}
lines = open("inputfull.txt").read().split("\n")

for line in lines:
    split_line = line.split(" ")
    hands[split_line[0]] = split_line[1]

print(hands)

for hand in hands:
    card_counts = Counter(hand)
    sorted_cards = sorted(card_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    length = len(sorted_cards)

    if length == 5:
        hand_types.setdefault("High card", []).append(hand)
    if length == 4:
        hand_types.setdefault("One pair", []).append(hand)
    if length == 3:
        if sorted_cards[0][1] == 3:
            hand_types.setdefault("Three of a kind", []).append(hand)
        else:
            hand_types.setdefault("Two pair", []).append(hand)
    if length == 2:
        if sorted_cards[0][1] == 4:
            hand_types.setdefault("Four of a kind", []).append(hand)
        else:
            hand_types.setdefault("Full house", []).append(hand)
    if length == 1:
        hand_types.setdefault("Five of a kind", []).append(hand)

strength = "AKQJT98765432"
for key, value in hand_types.items():
    hand_types[key] = sorted(value, key=lambda x: [strength.index(card[0]) for card in x])

final_list = []
for key, value in hand_types.items():
    final_list += value

final_list.reverse()

score = 0
for i, hand in enumerate(final_list):
    score += (i + 1) * int(hands[hand])

print("Total Score : %s" % score)
