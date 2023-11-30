#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows for Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle
        up to the nth row.

    Note:
        Returns an empty list if n <= 0.
        Assumes n will always be an integer.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        row = [1]
        # Compute values for the current row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        # Append the current row to the triangle
        triangle.append(row)

    return triangle
