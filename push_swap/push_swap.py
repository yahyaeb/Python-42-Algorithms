#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <number arguments>")
        sys.exit(1)
    a = []
    b = []
    try:
        for i in sys.argv[1:]:
            a.append(int(i))
    except ValueError:
        print("invalid input: all arguments must be integers")
        sys.exit(1)
    a_sorted = sorted(a)
    sort_list(a, b, a_sorted)


def sa(a):
    """
        Swap the first two elements of stack.
    """
    if(len(a) >= 2):
        a[0], a[1] = a[1], a[0]
        
        
def sb(b):
    """
        Swap the first two elements of stack.
    """
    if(len(b) >= 2):
        b[0], b[1] = b[1], b[0]
        
def ss(a, b):
    """
        Swap the first two elements of both stacks given.
    """
    if(len(a) >= 2):
        a[0], a[1] = a[1], a[0]
    if(len(b) >= 2):
        b[0], b[1] = b[1], b[0]

def pa(a, b):
    """
        Push the top element from stack b onto stack a.
    """
    if(len(b) > 0):
        a.insert(0, b[0])
        b.pop(0)

def pb(a, b):
    """
        Push the top element from stack a onto stack b.
    """
    if(len(a) > 0):
        b.insert(0, a[0])
        a.pop(0)

def ra(a):
    """
        Rotate stack a upwards by moving the first element to the end.
    """
    if(len(a) >= 2):
        a.append(a[0])
        a.pop(0)

def rb(b):
    """
        Rotate stack b upwards by moving the first element to the end.
    """
    if(len(b) >= 2):
        b.append(b[0])
        b.pop(0)

def rr(a , b):
    """
        Rotate both stacks a and b upwards at the same time.
    """
    if(len(a) >= 2 ):
        a.append(a[0])
        a.pop(0)
    if(len(b) >= 2):
        b.append(b[0])
        b.pop(0)

def rra(a):
    """
        Reverse rotate stack a by moving the last element to the front.
    """
    if(len(a) >= 2):
        a.insert(0, a[len(a) -1])
        a.pop(len(a) -1)


def rrb(b):
    """
        Reverse rotate stack b by moving the last element to the front.
    """
    if(len(b) >= 2):
        b.insert(0, b[len(b) -1])
        b.pop(len(b) -1)

def rrr(a, b):
    """
    rotates both stacks in reverse: the last element of each stack becomes the first element.
    """
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

def push_to_stack_b(a, b, index):
    if index < 0:
        return 
    target = a[index]
    while(a[0] != target):
        index = a.index(target)
        if(index <= len(a) /2):
            print("ra")
            ra(a)
        else:
            print("rra")
            rra(a)
    pb(a, b)
    print("pb")

def find_closes_in_range(stack, min , max):
    closest_index = -1
    current_index = 0
    for i in stack:
        if(i >= min and i <= max):
            return current_index
        current_index+=1
    return closest_index

def bring_to_top_b(b, a, index):
        if(index < 0):
            return
        target = b[index]
        while b[0] != target:
            index = b.index(target)
            if index <= len(b) //2:
                print("rb")
                rb(b)
            else:
                print("rrb")
                rrb(b)

def sort_three(a, sorted_list):
    if(len(a) < 2):
        return
    elif (len(a) == 2 and a != sorted_list):
        print("sa")
        sa(a)
        return
    elif(a == sorted_list):
        return
    if(a.index(max(a)) == 0):
        print("ra")
        ra(a)
    elif(a[1] == max(a)):
        print("rra")
        rra(a)
    if(a[0] > a[1]):
        print("sa")
        sa(a)

def sort_five(a, b, sorted_list):
    if(a == sorted_list):
        return
    while len(a) > 3:
        if(a.index(min(a)) <= len(a) / 2):
            while a.index(min(a)) > 0:
                print("ra")
                ra(a)
        else:
            while a.index(min(a)) < len(a) and a.index(min(a)) > len(a) /2:
                print("rra")
                rra(a)
        pb(a, b)
        print("pb")
    sort_three(a,b)
    while len(b) > 0:
        print("pa")
        pa(a,b)


def sort_list(a, b, sorted_list):
    while a != sorted_list:
        if len(a) > 5:
            chunk_size = 20
            curr_min = min(a)
            curr_max = curr_min + chunk_size
            while a:
                while has_elements_in_range(a, curr_min, curr_max):
                    target_index = find_closes_in_range(a, curr_min, curr_max)
                    push_to_stack_b(a, b, target_index)
                curr_min += chunk_size
                curr_max += chunk_size
            while b:
                max_index = b.index(max(b))
                bring_to_top_b(b, a, max_index)
                pa(a, b)
                print("pa")
        elif(len(a) > 3 and len(a) <= 5):
            sort_five(a,b, sorted_list)
        elif(len(a) <= 3):
            sort_three(a, sorted_list)

main()