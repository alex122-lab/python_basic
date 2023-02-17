import random
class Card:

    def __init__(self, suit, rank, val):
        self.suit = suit #   - масть
        self.rank = rank #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
        self.val = val

class Deck:

    def __init__(self):
        ranks = [['2',2],['3',3],['4',4],['5',5],['6',6],['7',7],['8',8],['9',9],['10',10],['Jack',10],['Queen',10],
                 ['King',10],['Ace',11]]

        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

        values = [2,3,4,5,6,7,8,9,10,10,10,10,11]

        self.cards = [Card(suit,rank,val) for rank,val in ranks for suit in suits]

class Player:

    def __init__(self, name, desk, list_cards):
        self.name = name #  - имя
        self.desk = desk # - колода карт
        self.list_cards = list_cards #  карты на руках

    def info(self):
        print(f'Игрок {self.name} '
              f'имеет на руках {len(self.list_cards)} карт')
        for card in self.list_cards:
            print(f'ранг карты - {card.rank}, '
                  f'масть карты - {card.suit}, '
                  f'ценовое значение карты - {card.val} очков')
        print(f'всего очков - {self.count}')

    def player_hand(self): # игрок
        self.count = 0
        for card in self.list_cards:
            if card.rank != 'Ace':
                self.count += int(card.val)
        for card in self.list_cards:
            if card.rank == 'Ace':
                if self.count > 11:
                    self.count += 1
                else:
                    self.count += int(card.val)

    def distribution_cards(self, deck, count):
        random.shuffle(deck.cards)
        new_card = random.sample(deck.cards, count)
        self.list_cards += new_card
        for card in new_card:
            deck.cards.remove(card)
#
deck = Deck()
player = Player('Иван', deck, [])
computer = Player('Computer', deck, [])

player.distribution_cards(deck, 2)
player.player_hand()
player.info()
computer.distribution_cards(deck, 2)
computer.player_hand()

while True:
    number = int(input('Взять карту - введите 1, остановиться - введите 0: '))
    if number == 1 and len(deck.cards) >= 2:
        player.distribution_cards(deck, 1)
        player.player_hand()
        player.info()
        computer.distribution_cards(deck, 1)
        computer.player_hand()
    else:
        break

if computer.count < player.count <= 21:
    print(f'{player.name} выиграл')
elif computer.count == player.count <= 21:
    print(f'ничья')
else:
    print(f'{player.name} проиграл')

