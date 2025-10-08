#!/usr/bin/env python3

def ft_memcmp(b1, b2, n):
    for i in range(n):
        if(b1[i] != b2[i]):
            return b1[i] - b2[i]
    return 0

# #test
# a = bytearray(b"hello")
# b = bytearray(b"heLLo")
# print(ft_memcmp(a, b, 4))