from sys import stdin

class Hand:  
  def __init__(self, cards, bid):
    self.cards = cards
    self.bid = bid
    self.s_cards = sorted(cards)
    self.counts = {c: self.s_cards.count(c) for c in set(cards)}
    self.has_j = 'J' in self.counts
    self.score = None
  
  def five(self):
    if len(self.counts) == 1:
      return True
    return self.has_j and len(self.counts) == 2

  def four(self):
    if (self.s_cards[0] == self.s_cards[3] or
        self.s_cards[1] == self.s_cards[4]):
      return True
    if not self.has_j:
      return False    
    for c in self.counts:
      if c == 'J':
        continue
      if self.counts[c] + self.counts['J'] == 4:
        return True
    return False 

  def full(self):
    if not self.has_j:
      return len(self.counts) == 2
    return len(self.counts) == 3

  def three(self):
    for c in self.counts:
      if self.counts[c] == 3:
        return True
    return self.has_j and len(self.counts) == 4

  def two(self):
    if not self.has_j:
      return len(self.counts) == 3
    return len(self.counts) == 4

  def one(self):
    if not self.has_j:
      return len(self.counts) == 4
    return len(self.counts) == 5

  def calc_score(self):
    if self.score:
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
      return 13
    if c == 'K':
      return 12
    if c == 'Q':
      return 11
    if c == 'T':
      return 10
    if c == 'J':
      return 1
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

