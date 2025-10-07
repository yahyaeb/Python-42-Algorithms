#!/usr/bin/env python3

def ft_strnstr(big, little, length):
    # Base cases
    if not big or length == 0:
        return None
    if not little:
        return big

    for i in range(min(len(big), length)):
        if i + len(little) > length:
            break
        if big[i:i + len(little)] == little:
            return big[i:] 
    return None


