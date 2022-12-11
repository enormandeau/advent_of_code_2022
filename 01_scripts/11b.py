#!/usr/bin/env python3
"""Solution to Advent of Code problem (see file name)

Usage:
    <program> input_file
"""

# Modules
import sys

# Parse user input
try:
    input_file = sys.argv[1]
except:
    print(__doc__)
    sys.exit(1)

# Functions
def inspect(m, monkeys, modulo):
    while monkeys[m]["items"]:

        monkeys[m]["inspected"] += 1

        if isinstance(monkeys[m]["operation"][1], int):
            second_value = monkeys[m]["operation"][1]
        else:
            second_value = monkeys[m]["items"][0]

        if monkeys[m]["operation"][0] == "+":
            monkeys[m]["items"][0] += second_value
        else:
            monkeys[m]["items"][0] *= second_value

        monkeys[m]["items"][0]  = monkeys[m]["items"][0] % modulo

        if monkeys[m]["items"][0] % monkeys[m]["divisor"]:
            monkeys[monkeys[m]["if_not_multiple"]]["items"].append(
                    monkeys[m]["items"].pop(0))
        else:
            monkeys[monkeys[m]["if_multiple"]]["items"].append(
                    monkeys[m]["items"].pop(0))

# Load data
monkeys = dict()
modulo = 1

with open(input_file) as infile:
    for line in infile:
        l = line.strip().split(" ")
        if l[0] == "Monkey":
            m = int(l[1].replace(":", ""))
            monkeys[m] = dict()

            monkeys[m]["items"] = [int(x)for x in next(infile).strip().replace(",", "").split(" ")[2:]]
            monkeys[m]["operation"] = next(infile).strip().replace(",", "").split(" ")[4:]
            try:
                monkeys[m]["operation"][1] = int(monkeys[m]["operation"][1])
            except:
                pass

            monkeys[m]["divisor"] = int(next(infile).strip().replace(",", "").split(" ")[3:][0])
            modulo *= monkeys[m]["divisor"]
            monkeys[m]["if_multiple"] = int(next(infile).strip().replace(",", "").split(" ")[5:][0])
            monkeys[m]["if_not_multiple"] = int(next(infile).strip().replace(",", "").split(" ")[5:][0])
            monkeys[m]["inspected"] = 0

# Solve problem
for round in range(10000):
    for m in sorted(monkeys):
        inspect(m, monkeys, modulo)

# Solution 1
print("Solution to problem 1:\n")

most = sorted([monkeys[m]["inspected"] for m in monkeys])[-2:]
print(most[0] * most[1])
