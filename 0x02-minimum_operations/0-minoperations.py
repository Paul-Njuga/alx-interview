#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    In a text file, there's a single character H.
    The text editor can execute only two operations,
    in the file: Copy All and Paste. Given a number n,
    Calculate the fewest no. of ops that result in,
    exactly n H characters in the file
    """
    if n <= 1:
        return 0
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op
