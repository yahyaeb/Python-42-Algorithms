#!/usr/bin/env python3

import sys

def get_next_line(file_object):
    for line in file_object:
        yield line.rstrip('\n')

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename) as file:
            for line in get_next_line(file):
                print(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)

main() 