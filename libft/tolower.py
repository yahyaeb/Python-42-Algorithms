#!/usr/bin/env python3

def ft_tolower(x):
    if ('A' <= x <= 'Z'):
        return (chr(ord(x) + 32))
    else:
        return (x)
print(ft_tolower("S"))