#!/usr/bin/env python3

def ft_strrchr(str, c):
    if not str:
        return None
    pos = 0
    last_pos = -1
    for i in str:
        if(i == c):
            last_pos = pos
        pos+=1
    return last_pos if last_pos != -1 else None

#test
print(ft_strrchr("yahya", "y"))