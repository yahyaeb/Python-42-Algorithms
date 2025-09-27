#!/usr/bin/env python3

def ft_isascii(x):
    #ord() to get the ascii value of x
    return 0 <= ord(x) <= 127

# print(ft_isascii('3'))
# print(ft_isascii('#'))
# print(ft_isascii(')'))
# print(ft_isascii('x'))
# print(ft_isascii('!'))
