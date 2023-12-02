import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 0:
  input = open(DEF_FILE)
else:
  input = sys.stdin


