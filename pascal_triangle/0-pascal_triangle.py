#!/usr/bin/python3
""" List of Pascal triangle """
def pascal_triangle(n):
  """ Pascal Triangle """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            element = prev_row[j - 1] + prev_row[j]
            row.append(element)

        row.append(1)
        triangle.append(row)

    return triangle
