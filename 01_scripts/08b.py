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
scores = [[0 for y in list(x.strip())] for x in open(input_file).readlines()]

# Scan forest to find visibility_scores
dimx = len(forest[0])
dimy = len(forest)
max_score = 0

for y in range(dimy):

    for x in range(dimx):

        tree_height = forest[y][x]

        left  = forest[y][:x][::-1]
        right = forest[y][x+1:]
        up    = [forest[yy][x] for yy in range(y)][::-1]
        down  = [forest[yy][x] for yy in range(y+1, dimy)]

        directions = [left, right, up, down]
        score = 1

        for d in directions:
            dist = 0

            while d:
                height = d.pop(0)

                dist += 1

                if height >= tree_height:
                    break

            score *= dist

        if score > max_score:
            max_score = score

        print(x, y, "score:", score)

# Solution 2
print("\nSolution to problem 2:\n")
print(max_score)
