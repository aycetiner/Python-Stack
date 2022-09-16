def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30

        >>> m3 = [
        ...    [1, 2, 3, 4],
        ...    [5, 6, 7, 8],
        ...    [9, 10, 11, 12],
        ...    [13, 14, 15, 16]
        ... ]
        >>> sum_up_diagonals(m3)
        68
    """
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i] + matrix[i][-(i + 1)]

    return total
