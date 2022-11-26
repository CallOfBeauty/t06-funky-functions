######################################################################
# Authors: Justin - Dimitrios
# Username: robertsj2, ntentia
#
# Assignment: T06: Funky Functions Test Suite
# Purpose:  A fruitful function to be tested by my partner.
#
######################################################################
import math
def hypo(a, b):
    a_square = a**2
    b_square = b**2
    c_square = a_square + b_square
    c = math.sqrt(c_square)
    return c
def main():
    w = hypo(1, 2)
    print(w)
if __name__ == "__main__":
    main()