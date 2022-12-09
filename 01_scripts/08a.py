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

# Load data
forest = [[int(y) for y in list(x.strip())] for x in open(input_file).readlines()]
visibility = [[0 for y in list(x.strip())] for x in open(input_file).readlines()]

# Scan forest to update visibility
num_visible = 0
dimx = len(forest[0])
dimy = len(forest)

# Check from left
for y in range(dimy):
    
    max_height = 0
    first = True

    for x in range(dimx):
        height = forest[y][x]

        if first or height > max_height:
            first = False
            max_height = height
            if visibility[y][x] == 0:
                num_visible += 1

            visibility[y][x] += 1

# Check from left
for y in range(dimy):
    
    max_height = 0
    first = True

    for x in range(dimx)[::-1]:
        height = forest[y][x]

        if first or height > max_height:
            first = False
            max_height = height
            if visibility[y][x] == 0:
                num_visible += 1

            visibility[y][x] += 2

# Check from top
for x in range(dimx):
    
    max_height = 0
    first = True

    for y in range(dimy):
        height = forest[y][x]

        if first or height > max_height:
            first = False
            max_height = height
            if visibility[y][x] == 0:
                num_visible += 1

            visibility[y][x] += 4

# Check from top
for x in range(dimx):
    
    max_height = 0
    first = True

    for y in range(dimy)[::-1]:
        height = forest[y][x]

        if first or height > max_height:
            first = False
            max_height = height
            if visibility[y][x] == 0:
                num_visible += 1

            visibility[y][x] += 8

# Solution 1
print("Solution to problem 1:\n")
print(num_visible)
