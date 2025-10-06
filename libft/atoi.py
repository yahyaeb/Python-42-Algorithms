#!/usr/bin/env python3

def ft_atoi(s):
    if s.startswith('-'):
        num_part = s[1:]
    else:
        num_part = s

    if num_part.isdigit():
        return int(s)
    else:
        return "invalid"

    
print(ft_atoi("123"))     # 123
print(ft_atoi("-456"))    # -456
print(ft_atoi("12a3"))    # invalid
print(ft_atoi("--12"))    # invalid
