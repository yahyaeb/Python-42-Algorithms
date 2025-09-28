#!/usr/bin/env python3

def ft_toupper(x):
    if ('a' <= x <= 'z'):
        return (chr(ord(x) - 32))
    else:
        return (x)

print(ft_toupper("S"))