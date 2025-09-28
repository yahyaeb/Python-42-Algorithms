#!/usr/bin/env python3

def ft_strncmp(str1, str2, num):
    for i in range(num):
        c1 = ord(str1[i]) if i < len(str1) else 0
        c2 = ord(str2[i]) if i < len(str2) else 0
        if c1 != c2:
            return c1 - c2
    return 0
