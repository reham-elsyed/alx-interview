#!usr/bin/python3
"""
counting minimum number of operations
"""

def minOperations(n):
    operations = 0
    while True:
        if n <= 1:
            break
        n *= 2
        operations += 1
    while n > 1:
        n -= 1
        operations += 1

    return operations