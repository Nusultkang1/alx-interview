#!/usr/bin/python3
"""
Creates a function def pascal_triangle(n)
Returns a list of lists of integers
represents the pascal's triangle of n rows
Returns and empty list if n <= 0
"""

def print_pascal_triangle(n):
    """
    function that prints pascal's triangle of
    n rows if n > 0, and returns an empty list if n <= 0
    """

    triangle = []

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                element = 1
            else:
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
        triangle.append(row)

    for row in triangle:
        for element in row:
            print(element, end=' ')
        print()

