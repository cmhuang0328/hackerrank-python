#! /usr/bin/env python3
'''
Task
Given an integer, , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

Input Format
A single line containing a positive integer, n.

Constraints
1 <= n <= 100 
'''

if __name__ == '__main__':
    n = int(input())
    # range function (x, y) means x to y - 1
    if ( n in range(6, 21) or n % 2.0 == 1):
        print("Weird")
    else:
        print("Not Weird")
