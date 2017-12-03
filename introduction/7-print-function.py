#! /usr/bin/env python3

'''
Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.

Input Format 
The first line contains an integer N.

Output Format 
Output the answer as explained in the task.
'''

if __name__ == '__main__':
    n = int(input())
    # use * to "unpack" a list so that it becomes arguments instead of a list.
    # use sep= '' to get 123..n w/o spaces
    print (*range(1, n+1), sep='')

