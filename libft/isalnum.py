#!/usr/bin/env python3
import isalpha
import isdigit

def ft_isalnum(x):
    return isdigit.ft_isdigit(x) or isalpha.ft_isalpha(x)

print(ft_isalnum('a'))  # True
print(ft_isalnum('7'))  # True
print(ft_isalnum('#'))  # False