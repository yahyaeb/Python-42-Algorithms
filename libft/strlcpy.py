#!/usr/bin/env python3

def ft_strlcat(dst, src, dstsize):
    results = dst + src
    new_dest = ""
    for i, chr in enumerate(results):
        if(i < dstsize):
            new_dest+=chr
    return (new_dest, len(dst) + len(src))

# dst = "Hola"
# src = "yassine"

# results = ft_strlcat(dst, src, 5)

# print(results)