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

head = (0, 0)
tail = (0, 0)
visited = set()

for m in moves:
    d, num = m[0], int(m[1])
    #print(d, num, head, tail)

    # Move head
    for _ in range(num):
        head = (head[0] + dirs[d][0], head[1] + dirs[d][1])
        #print("   ", head, tail, end=" - ")
 
        # Move tail
        if head == tail:
            pass
            #print("[ NA- overlapping ]")

        elif max_dist(head, tail) <= 1:
            pass
            #print("[ NA- adjacent]")

        elif same_row(head, tail):
            tail = ((tail[0] + head[0])//2, tail[1])
            #print("same row ->", head, tail)

        elif same_col(head, tail):
            tail = (tail[0], (tail[1] + head[1])//2)
            #print("same column ->", head, tail)

        elif max_dist(head, tail) > 1:
            diag = diag_move(head, tail)
            tail = (tail[0] + diag[0], tail[1] + diag[1])
            #print("NEED TO MOVE DIAGONALLY:", head, tail)

        elif min_dist(head, tail) <= 1:
            pass
            #print("[ NA- adjacent    ]")

        visited.add(tail)
    #print()

# Solution 1
print("Solution to problem 1:\n")
print(len(visited))


# Solution 2
#print("\nSolution to problem 2:\n")

