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
def max_dist(a, b):
    """Return max horizontal or vertical distance
    """
    return max([abs(a[0] - b[0]), abs(a[1] - b[1])])

def min_dist(a, b):
    """Return min horizontal or vertical distance
    """
    return min([abs(a[0] - b[0]), abs(a[1] - b[1])])

def same_row(a, b):
    return a[1] == b[1]

def same_col(a, b):
    return a[0] == b[0]

def diag_move(a, b):
    xdiff = a[0] - b[0]
    ydiff = a[1] - b[1]

    return ((xdiff > 0) - (xdiff < 0), (ydiff > 0) - (ydiff < 0))

# Load data
moves = [x.strip().split(" ") for x in open(input_file).readlines()]

dirs = {
        "R": ( 1,  0),
        "L": (-1,  0),
        "U": ( 0,  1),
        "D": ( 0, -1)
        }

# Initialize rope
rope = {}
parts = range(10)

for p in parts:
    rope[p] = (0, 0)

visited = set()

for m in moves:
    d, num = m[0], int(m[1])

    # Move parts
    for _ in range(num):
        rope[0] = (rope[0][0] + dirs[d][0], rope[0][1] + dirs[d][1])
     
        for p in parts[1:]:
            # Move part
            if rope[p-1] == rope[p]:
                pass

            elif max_dist(rope[p-1], rope[p]) <= 1:
                pass

            elif same_row(rope[p-1], rope[p]):
                rope[p] = ((rope[p][0] + rope[p-1][0])//2, rope[p][1])

            elif same_col(rope[p-1], rope[p]):
                rope[p] = (rope[p][0], (rope[p][1] + rope[p-1][1])//2)

            elif max_dist(rope[p-1], rope[p]) > 1:
                diag = diag_move(rope[p-1], rope[p])
                rope[p] = (rope[p][0] + diag[0], rope[p][1] + diag[1])

            elif min_dist(rope[p-1], rope[p]) <= 1:
                pass

        visited.add(rope[9])

# Solution 2
print("\nSolution to problem 2:\n")
print(len(visited))
