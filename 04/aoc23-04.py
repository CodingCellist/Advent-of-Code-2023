import re
import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# PART 1 #

def parse_card(line: str):
  # start by splitting into winning and haves
  raw_wins, raw_haves = line.split('|')
  # then remove the "Card \d+:" part from `raw_wins`
  raw_wins = raw_wins.split(':')[-1]
  # finally, cast to a list of actual numbers
  wins = [ int(n) for n in raw_wins.split(' ') if n != '' ]
  haves = [ int(n) for n in raw_haves.split(' ') if n != '' ]
  # and return as a dict with sensibly named keys
  return {"wins": wins, "haves": haves}


# Part 2 #

# Given a current queue of the number of copies, accumulate the new number of
# copies to their respective entries. We can be clever about this and never
# store the literal string copies of the cards by simply multiplying the number
# of new copies by the current multiplier.
#
# Note that since we're only iterating over the new counts, and the puzzle has
# told us we will not move past the table end, `i` is always a valid index
def acc_copies(n_copies_queue: list, n_cards: int, n_winning: int):
  for i in range(n_winning):
    # if we're adding a number of copies for a card we've not seen yet,
    # append/extend the list with a new entry containing that many copies
    if i >= len(n_copies_queue):
      n_copies_queue.append(n_cards)
    # otherwise, update with the extra number of copies
    else:
      n_copies_queue[i] += n_cards
  return n_copies_queue


# SOLUTION #

# FIXME: only for testing
input = [ "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        , "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
        , "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
        , "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"
        , "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"
        , "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        ]

total_pts = 0

# to be treated as a queue
n_copies = []
cascading_pts = 0

for line in input:
  # get the winning and obtained numbers
  card = parse_card(line)

  # count the number of winning cards
  n_winning = len([ x for x in card["haves"] if x in card["wins"] ])

  # Yes this is technically O(n) and I should be using `collections.deque`, no I
  # can't be bothered for this small a problem
  # If the queue is empty, there are no copies to count
  n_cards = 1 if len(n_copies) == 0 else 1 + n_copies.pop(0)

  n_copies = acc_copies(n_copies, n_cards, n_winning)

  # and at this point, if we have any winning numbers, the points are just
  # powers of 2 (`n_wins - 1` since first power is 2^0)
  if n_winning != 0:
    pts = pow(2, n_winning - 1)
    # part-1
    total_pts += pts
    # part-2, remembering to include the original card
    cascading_pts += pts * n_cards

print(f"Part 1 (sum): {total_pts}")
print(f"Part 2 (w. copies): {cascading_pts}")

# too high: 403657723988791919
# too high: 41681179
#
# FIXME: BE THE MACHINE!
# Card 1: 4 matched =>  0 copies => [1, 1, 1, 1] => (1 +  0) * 8 = 8 pts
# Card 2: 2 matched =>  1 copy   =>    [3, 3, 1] => (1 +  1) * 2 = 4 pts
# Card 3: 2 matched =>  3 copies =>       [7, 5] => (1 +  3) * 2 = 8 pts
# Card 4: 1 matched =>  7 copies =>         [13] => (1 +  7) * 1 = 8 pts
# Card 5: 0 matched => 13 copies =>           [] => (1 + 13) * 0 = 0 pts
# Card 6: 0 matched =>  0 copies =>           [] => (1 +  0) * 0 = 0 pts
