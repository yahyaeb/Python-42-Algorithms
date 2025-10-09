#!/usr/bin/env python3

def ft_memset(array, value, size):
    for i in range(min(size, len(array))):
        array[i] = value
    return array

# buf = bytearray(b"abcdef")
# ft_memset(buf, ord('X'), 3)
# print(buf)  # b'XXXdef'
