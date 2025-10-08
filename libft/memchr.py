#!/usr/bin/env python3

def ft_memchr(data, searchedVal, size):
    for i, val in enumerate(data[:size]):
        if(val == searchedVal):
            return data[i:]
    return None

# #test   
# table = [10, 20, 40, 50, 60]
# print(ft_memchr(table, 20, 5))
