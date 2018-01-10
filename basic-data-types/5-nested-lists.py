#! /usr/bin/env python3
'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list 
and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second
line contains their grade.

Constraints

2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, 
order their names alphabetically and print each one on a new line.
'''

if __name__ == '__main__':
    marksheet = []
    for _ in range(0, int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    # Use join to select second_highest
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
