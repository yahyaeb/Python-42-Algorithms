#!/usr/bin/env python3
# | Operation | Stack(s) | Description (in words)                        |
# | --------- | -------- | --------------------------------------------- |
# | sa        | a        | Swap top two elements of a                    |
# | sb        | b        | Swap top two elements of b                    |
# | ss        | a & b    | Swap top two elements of both a and b         |
# | pa        | a, b     | Push top element from b onto a                |
# | pb        | a, b     | Push top element from a onto b                |
# | ra        | a        | Rotate a up (first element becomes last)      |
# | rb        | b        | Rotate b up                                   |
# | rr        | a & b    | Rotate both a and b up                        |
# | rra       | a        | Reverse rotate a (last element becomes first) |
# | rrb       | b        | Reverse rotate b                              |
# | rrr       | a & b    | Reverse rotate both a and b                   |


#operations: 
"""
    Swap the first two elements of stack.
    If the stack has fewer than 2 elements, do nothing.
    The operation modifies the stack in place.
"""
def sa(a):
    if(len(a) >= 2):
        a[0], a[1] = a[1], a[0]
        
        
def sb(b):
    if(len(b) >= 2):
        b[0], b[1] = b[1], b[0]
        
"""
    Swap the first two elements of both stacks given.
    only swap one that has more than 1 element
    The operation modifies the stack in place.
"""      
def ss(a, b):
    if(len(a) >= 2):
        a[0], a[1] = a[1], a[0]
    if(len(b) >= 2):
        b[0], b[1] = b[1], b[0]


"""
    Push the top element from stack b onto stack a.

    If stack b has no elements, do nothing.
    Modifies both stacks in place.
"""
def pa(a, b):
    if(len(b) > 0):
        a.insert(0, b[0])
        b.pop(0)

"""
    Push the top element from stack a onto stack b.

    If stack a has no elements, do nothing.
    Modifies both stacks in place.
"""
def pb(a, b):
    if(len(a) > 0):
        b.insert(0, b[0])
        a.pop(0)

def ra(a):
    if(len(a) >= 2):
        a.append(a[0])
        a.pop(0)

def rb(b):
    if(len(b) >= 2):
        b.append(b[0])
        b.pop(0)

def rr(a , b):
    if(len(a) >= 2 ):
        a.append(b[0])
        a.pop(0)
    if(len(b) >= 2):
        b.append(a[0])
        b.pop(0)

def rra(a):
    if(len(a) >= 2):
        a.insert(0, a[len(a) -1])
        a.pop(len(a) -1)


def rrb(b):
    if(len(b) >= 2):
        b.insert(0, b[len(b) -1])
        b.pop(len(b) -1)

def rrr(a, b):
    if(len(a) >= 2):
        a.insert(0, a[len(a) -1])
        a.pop(len(a) -1)
    if(len(b) >= 2):
        b.insert(0, b[len(b) -1])
        b.pop(len(b) -1)
def has_elements_in_range(list, min, max):
    for i in list:
        if(i >= min and i <= max):
            return 1
    return 0
        
a = []       
sorted_list = sorted(a)
while(a != sorted_list):
    if len(a) > 5:
        chunck_size = 20
        curr_min = min(a)
        curr_max = curr_min + chunck_size
        while(a):
            while(has_elements_in_range(a, curr_min, curr_max)):
                


a = [3, 2, 4]
b = [5, 4, 3]
print(f"before a=> {a} b=> {b}")
s = rrr(a, b)
print(f"after a=> {a} b=> {b}")