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
def increase_cycle(cycle, register, report_cycles, n):
    """Increase the cycle and report register if needed
    """
    global signal_strengts

    for i in range(cycle+1, cycle+n+1):
        if i in report_cycles:
            print(f"Cycle {i}: {register}\t[{i*register}]")
            signal_strengts.append(i*register)

    return cycle + n

# Load data
instructions = [x.strip().split(" ") for x in open(input_file).readlines()]

# Solve problem
cycle = 0
register = 1
report_cycles = range(20, 221, 40)
signal_strengts = []

for ins in instructions:
    if ins[0] == "noop":
        cycle = increase_cycle(cycle, register, report_cycles, 1)

    if ins[0] == "addx":
        x = int(ins[1])
        cycle = increase_cycle(cycle, register, report_cycles, 2)
        register += x

# Solution 1
print("Solution to problem 1:\n")
print(sum(signal_strengts))

