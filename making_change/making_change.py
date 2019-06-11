#!/usr/bin/python

import sys

def making_change(amount, denominations, cache = {}):
    counts = 0
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif amount in cache:
        return cache[amount]
    else:
        for d in range(len(denominations)):
            mon = denominations[d]
            counts += making_change(amount-mon, denominations[d:])
        cache[amount] = counts
        return counts

denominations = [1, 5, 10, 25, 50]
for i in range(1000):
    print("There are {} ways to make {} cents".format(making_change(i, denominations), i))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")