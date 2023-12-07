from sys import stdin

class Hand:  
  def __init__(self, cards, bid):
    self.cards = cards
    self.bid = bid
    self.s_cards = sorted(cards)
    self.set_cards = set(cards)
    self.score = None
  
  def five(self):
    return len(self.set_cards) == 1

  def four(self):
    return (self.s_cards[0] == self.s_cards[3] or
            self.s_cards[1] == self.s_cards[4])

  def full(self):
    return len(self.set_cards) == 2

  def three(self):
    for c in self.set_cards:
      if self.s_cards.count(c) == 3:
        return True
    return False

  def two(self):
    return len(self.set_cards) == 3

  def one(self):
    return len(self.set_cards) == 4

  def calc_score(self):
    if self.score is not None:
      return self.score
    if self.five():
      self.score = 6
    elif self.four():
      self.score = 5
    elif self.full():
      self.score = 4
    elif self.three():
      self.score = 3
    elif self.two():
      self.score = 2
    elif self.one():
      self.score = 1
    else:
      self.score = 0
    return self.score

  def c_to_int(c):
    if c == 'A':
      return 14
    if c == 'K':
      return 13
    if c == 'Q':
      return 12
    if c == 'J':
      return 11
    if c == 'T':
      return 10
    return int(c)

  def __lt__(self, other):
    if self.calc_score() == other.calc_score():
      for c1, c2 in zip(self.cards, other.cards):
        if c1 == c2:
          continue
        return Hand.c_to_int(c1) < Hand.c_to_int(c2)
      return True
    return self.calc_score() < other.calc_score()

hands = []
for line in stdin:
  cards, bid = line.split()
  hands.append(Hand(cards, int(bid)))
hands.sort()

total = 0
for i, hand in enumerate(hands):
  total += hand.bid * (i + 1)
print(total)

