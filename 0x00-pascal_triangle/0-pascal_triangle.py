#!/usr/bin/python3
def print_pascal_triangle(n):
    # Create an empty list to store the triangle
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

