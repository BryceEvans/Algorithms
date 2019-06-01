#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    allPossibilities = []

    options = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return [[]]
    else:
        prevPossibilities = rock_paper_scissors(n-1)
        for poss in prevPossibilities:
            for o in options:
                allPossibilities.append(poss + o)
        
        return allPossibilities

result = rock_paper_scissors(2)

for r in result:
    print(r)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')