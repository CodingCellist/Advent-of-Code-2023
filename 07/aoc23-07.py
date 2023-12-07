import re
import sys
from enum import Enum

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# Part 1 #


# for easy(?) ordering
class Card(Enum):
  A = 14
  K = 13
  Q = 12
  J = 11
  T = 10


# types of hand, in order of strength
class HandType(Enum):
  FIVE_KIND = 7
  FOUR_KIND = 6
  FULL_HOUSE = 5
  THREE_KIND = 4
  TWO_PAIR = 3
  ONE_PAIR = 2
  HIGH_CARD = 1


# Given a hand as a string, return a dict with the count of the number of cards
def count_hand(raw_hand: str):
  count = dict()
  for c in raw_hand:
    if c in count.keys():
      count[c] = count[c] + 1
    else:
      count[c] = 1


# Given a hand as a string, find its type
def categorise_hand(hand_count: dict):
  # only one entry means all cards were the same
  if len(hand_count) == 1:
    return HandType.FIVE_KIND
  # five entries means all cards were unique
  elif len(hand_count) == 5:
    return HandType.HIGH_CARD
  # two entries means a group of 3 and a group of 2
  elif len(hand_count) == 2:
    return HandType.FULL_HOUSE
  # four entries means a single pair
  elif len(hand_count) == 4:
    return HandType.ONE_PAIR
  # 3 entries means we've either got a full house three of kind
  elif len(hand_count) == 3:
    for v in hand_count.values():
      # if any of the counts was 3, we have three of a kind
      if v == 3:
        return HandType.THREE_KIND
    # otherwise, by elimination, there must be two pairs and a single
    return HandType.TWO_PAIR

  # give up on anything else; it shouldn't happen
  else:
    print("wat")
    exit(1)


# Is hand1 less-than hand2? If the types equal, start inspecting the individual
# cards
def hand_lt(hand1, hand2):
  if hand1['type'].value == hand2['type'].value:
    for card1, card2 in zip(hand1['cards'], hand2['cards']):
      if card1 == card2:
        continue

      return card1.value < card2.value

  return hand1['type'].value < hand2['type'].value



# SOLUTION #

input = [ "32T3K 765"
        , "T55J5 684"
        , "KK677 28"
        , "KTJJT 220"
        , "QQQJA 483"
        ]

for line in input:
