import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin


# PART-1 #

def get_digits(line: str):
  return [c for c in line if c.isdigit()]


# PART-2 #

lit_nums = { "one":   "o1ne"
           , "two":   "tw2o"
           , "three": "thr3ee"
           , "four":  "fo4ur"
           , "five":  "fi5ve"
           , "six":   "s6x"
           , "seven": "se7en"
           , "eight": "eig8ht"
           , "nine":  "ni9ne"
           , "zero":  "zer0o"
           }

def lit_to_digits(line: str):
  for lit, num in lit_nums.items():
    line = line.replace(lit, num)
  return line


# SOLUTION #

sum1 = 0
sum2 = 0
for line in input:
  # extract the digits
  digits = get_digits(line)
  # add the relevant parts to the sum
  sum1 += int(digits[0]) * 10 + int(digits[-1])

  digits = get_digits(lit_to_digits(line))
  print(digits)
  sum2 += int(digits[0]) * 10 + int(digits[-1])


print(f"Part 1: {sum1}")
print(f"Part 2: {sum2}")
