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

# Classes
class Directory:
    def __init__(self, name, parent=""):
        self.name = name
        self.parent = parent
        self.depth = directories[parent].depth + 1 if parent else 1
        self.dirs = []
        self.files = []
        self.size = 0

    def __repr__(self):
        to_print = [f"{self.name[-1]}/ {self.size}".replace("//", "/")]

        for f in self.files:
            to_print.append("  " * self.depth + f"{f[0]}: {f[1]}")

        for d in self.dirs:
            to_print.append("\n" + "  " * self.depth + str(directories[tuple(d)]))

        return "\n".join(to_print)

# Functions
def cd(rel_path):
    global path

    if rel_path == "..":
        path.pop()

    elif rel_path == "/":
        path = ["/"]

    else:
        # Check if path in current directory
        if tuple(path + [rel_path]) in directories[tuple(path)].dirs:
            path.append(rel_path)

        else:
            print(f"Error: No directory '{rel_path}' in '{'/' + '/'.join(path[1:])}'")

def ls(element):
    if element.startswith("dir"):
        rel_path = element.split(" ")[1]
        directories[tuple(path)].dirs.append(tuple(path + [rel_path]))
        directories[tuple(path + [rel_path])] = Directory(
                tuple(path + [rel_path]), parent=tuple(path))

    else:
        size, filename = element.split(" ")
        size = int(size)

        directories[tuple(path)].files.append((size, filename))

        for i in range(1, len(path) + 1):
            directories[tuple(path[:i])].size += size

# Read commands
commands = [x.strip().split("\n") for x in open(input_file).read().strip().split("$") if x]

# Initiate directory tree
path = [("/",)]
directories = {}
directories[("/",)] = Directory(("/", ))

# Execute commands
for c in commands:

    if c[0].startswith("cd "):
        rel_path = c[0].split(" ")[1]
        cd(rel_path)

    elif c[0] == "ls":
        for element in c[1: ]:
            ls(element)

# Get answer
big_size = 100000
small_dirs = [x for x in directories if directories[x].size <= big_size]

print(sum([directories[x].size for x in small_dirs]))
