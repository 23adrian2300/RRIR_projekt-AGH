from B_L import B, L
import numpy as np


def create_matrix_B(nof): # macierz wypełniona wartościami B
    matrix = [[0 for _ in range(nof)] for _ in range(nof)]
    for i in range(nof):
        for j in range(nof):
            if (abs(i - j) == 1):
                s = 2. * np.maximum(0, np.minimum(i, j) / nof)
                e = 2. * np.minimum(1, np.maximum(i, j) / nof)
            else:
                s = 2. * np.maximum(0, (i - 1) / nof)
                e = 2. * np.minimum(1, (i + 1) / nof)
            matrix[i][j] = B(j, i, s, e, nof)
    return matrix



def create_matrix_L(nof): # macierz wypełniona wartościami L
    elem_num = nof
    matrix = [0]*nof
    for i in range(elem_num):
        s = 2. * max(0, (i - 1) / elem_num)
        e = 2. * min(1, (i + 1) / elem_num)
        matrix[i] = (L(i, s, e, nof))
    return matrix
