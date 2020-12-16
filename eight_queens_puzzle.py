# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:06:31 2020

@author: mehme
"""

import sys
def test(did_pass): 
    # """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    
    print(msg)

# There are different representations
bd1 = [[0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1],
[0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0],
[1,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0]]

bd2 = [ "a6", "b4", "c2", "d0", "e5", "f7", "g1", "h3" ]
bd3 = [(0,6), (1,4), (2,2), (3,0), (4,5), (5,7), (6,1), (7,3)]
bd4 = [6, 4, 2, 0, 5, 7, 1, 3]


def share_diagonal(x0,y0,x1,y1): # any two or more queens can't be on diagonal
    """ Is  (x0,y0) on a shared diagonal with (x1,y1)? """
    dy = abs(y1-y0) #  the absolute y distance
    dx = abs(x1-x0) #  the absolute x distance
    
    return dx == dy
test(not share_diagonal(5,2,2,0))
test(share_diagonal(5,2,3,0))
test(share_diagonal(5,2,4,3))
test(share_diagonal(5,2,4,1))



def col_clashes(bs,c): # column check
    """ Return True if the queen at column c clashes with any queen to its left. """
    
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    
    return False

test(not col_clashes([6,4,2,0,5], 4))
test(not col_clashes([6,4,2,0,5,7,1,3], 7))


test(col_clashes([0,1], 1))
test(col_clashes([5,6], 1))
test(col_clashes([6,5], 1))
test(col_clashes([0,6,4,3], 3))
test(col_clashes([5,0,7], 2))
test(not col_clashes([2,0,1,3], 1))
test(col_clashes([2,0,1,3], 2))


def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False
test(not has_clashes([6,4,2,0,5,7,1,3])) 
test(has_clashes([4,6,2,0,5,7,1,3])) # Swap rows of first two
test(has_clashes([0,1,2,3])) # Try small 4x4 board
test(not has_clashes([2,0,3,1])) # Solution to 4x4 case

#part 2
def main():
    import random
    rng = random.Random()
    
    bd = list(range(8))
    num_found = 0
    tries = 0
    
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1 
        
        if not has_clashes(bd):
            print("Found solution {} in {} tries".format(bd,tries))
            tries = 0
            num_found += 1
main()
    