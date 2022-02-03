#!/usr/bin/python3
"""Define a function"""
"""Function pascal_triangle"""


def pascal_triangle(n):
    """Print the triangle of Pascal"""

    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i +1] = sum(rows[n - 1][i:i + 2])
    return(rows)
