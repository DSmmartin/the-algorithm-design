"""
Problem: Sorting
Input: A sequence of n keys a1,...,an.
Output: The permutation (reordering) of the input sequence such that:
a'1 <= a'2 <= ... <= a'n-1 <= a'n

Note that we seek algorithms taht are correct and efficient, while being easy to implement. But, may not be simultaneously achievable.
"""

def insertion_sort(sequence: list[int]) -> list[int]:
    """Notes:
    1. simple
    2. efficient in short Vs not-efficient in larger lists
    3. adaptive
    4. stable
    5. in-place
    6. online
    """
    for i in range(len(sequence)):
        j = i
        while ((j > 0) & (sequence[j] < sequence[j - 1])):
            sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
            j -= 1
    return sequence
