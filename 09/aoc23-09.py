import sys
from collections import deque

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# Part 1 #


# given a history of values and an accumulator, find the sequences
def find_seqs(history: list[int], acc_seqs: deque[list[int]]) -> deque[list[int]]:
  # start by creating the steps
  steps = [v2 - v1 for v1, v2 in zip(history, history[1:])]
  # if steps are 0, we're done
  if all([step == 0 for step in steps]):
    return acc_seqs
  # otherwise, we have a new sequence so accumulate it and recurse on the result
  else:
    # appendleft (effectively "cons") to more easily be able to sum the values
    # at extrapolation time
    acc_seqs.appendleft(steps)
    return find_seqs(steps, acc_seqs)


# Given a list of sequences, extrapolate the next value
# (should be easy thanks to Python's list index magic, methinks)
def extrapolate(seqs: deque[list[int]]) -> int:
  val = None
  # the extrapolated value is the result of accumulating each step in order
  for seq in seqs:
    step = seq[-1]
    if val is None:
      val = step
    else:
      val += step
  return val



# SOLUTION #

# FIXME: only for testing
##input = [ "0 3 6 9 12 15"
##        , "1 3 6 10 15 21"
##        , "10 13 16 21 30 45"
##        ]

extrap_sum = 0

for line in input:
  hist = [int(i) for i in line.split()]
  seqs = find_seqs(hist, deque([hist]))
  ##print(seqs)
  ##print(extrapolate(seqs))
  extrap_sum += extrapolate(seqs)

print(f"Part 1: {extrap_sum}")
