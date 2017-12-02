# Python 3
'''
Task 
Read an integer N. For all non-negative integers i < N, print i^2. See the sample for details.

Input Format

The first and only line contains the integer, N.

Constraints
1 <= N <= 20
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if n in range(0, 21):
            print (i ** 2)


