#!/usr/bin/env python3

def ft_strchr(str, c):
    pos = 0
    for i in str:
        if(i == c):
            return pos
        pos+=1
    return None
