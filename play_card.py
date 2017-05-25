import random

card_num = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
card_suit = ['hearts', 'spade', 'club', 'diamond']

def generatecards():
    poker = []
    for i in card_suit:
        for j in card_num:
            poker.append(i + j)
    poker.append('Joker')
    poker.append('joker')
    return poker

def playcard(cards):
    player1 = []
    player2 = []
    player3 = []

    random.shuffle(cards)
    for i in range(0,51):
        if i % 3 == 0:
            player1.append(cards[i])
        elif i % 3 == 1:
            player2.append(cards[i])
        else:
            player3.append(cards[i])
    print("player1:", end=' ')
    for card in player1:
        print(''.join(card), end=' ')
    print("\n")
    print("player2:", end=' ')
    for card in player2:
        print(''.join(card), end=' ')
    print("\n")
    print("player3:", end=' ')
    for card in player3:
        print(''.join(card), end=' ')
    print("\n")
    print("rest card:", end=' ')
    rest_card = cards[-3:]
    for card in rest_card:
        print(''.join(card), end=' ')





if __name__ == '__main__':
    poker = generatecards()
    print(poker)
    playcard(poker)