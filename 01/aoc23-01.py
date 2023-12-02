import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# PART-1 #

sum = 0
for line in input:
  # extract the digits
  digits = [c for c in line if c.isdigit()]
  # add the relevant parts to the sum
  sum += int(digits[0]) * 10 + int(digits[-1])

print(f"Part 1: {sum}")
