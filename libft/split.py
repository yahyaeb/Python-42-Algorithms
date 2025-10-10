#!/usr/bin/env python3

def ft_split(s, sep):
    table = []
    new_pos = 0
    for i, letter in enumerate(s):
        if letter == sep:
            table.append(s[new_pos:i])
            new_pos = i + 1
    table.append(s[new_pos:])
    return table

# #test
# sentence = "hello this is yahya"
# print(ft_split(sentence, ' '))
