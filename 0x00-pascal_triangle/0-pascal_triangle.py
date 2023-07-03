#!/usr/bin/python3
"""An interview challenge to represent pascal's triangle with a list of lists"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(row):
                row[j] = pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1]

        pascal_triangle[i] = row

    return pascal_triangle
