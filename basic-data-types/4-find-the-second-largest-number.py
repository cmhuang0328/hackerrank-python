#! /usr/bin/env python3
'''
You are given n numbers. Store them in a list and find the second largest number.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2 <= n <= 10
-100 <= A[i] <= 100
Output Format

Print the value of the second largest number.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # use sorted to sort the list with [-2] to find the second largest
    print (sorted(list(set(arr)))[-2])
