import numpy as np
from Create_Matrices import create_matrix_B, create_matrix_L


def solution(nof): #nof - number of elements

    mat_B = np.array(create_matrix_B(nof))
    mat_L = np.array(create_matrix_L(nof))

    mat_B_inv = np.linalg.inv(mat_B) # tworzenie macierzy odwrotniej
    sol = np.dot(mat_B_inv, mat_L) # obliczenie wartości U - tablica z wartościami dla odpowiednich przedziałów
    sol = np.append(sol, 0)
    return sol
