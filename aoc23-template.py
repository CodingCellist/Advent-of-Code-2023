import sys

DEF_FILE = "./input"

# read the file
input = None
if len(sys.argv) == 1:    # recall that argv[0] == program name
  input = open(DEF_FILE)
else:
  input = sys.stdin



# SOLUTION #

# FIXME: only for testing
input = [ ""
        ]

for line in input:
