#!/usr/bin/env python3

def ft_isprint(x):
    return len(x) == 1 and 32 <= ord(x) <= 126

print(ft_isprint("3"))    # True
print(ft_isprint(" "))    # True
print(ft_isprint("\n"))   # False